#!/usr/bin/env python3
"""S4 pretest runner — between-subject A/B stub for Synthetic User Lab.

Default: mock mode (no network). Optional LLM via SUL_RUNNER_MODE=llm + OPENAI_API_KEY.
Aligned with docs/course/sul/templates/pretest-protocol.md.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_PERSONAS = ROOT / "seed_data" / "personas.jsonl"
DEFAULT_VARIANTS = ROOT / "seed_data" / "variants.json"


def load_personas(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if not rows:
        raise SystemExit(f"No personas in {path}")
    return rows


def load_variants(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def stable_rng(seed: str) -> random.Random:
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return random.Random(int(digest[:16], 16))


def assign_between_subject(
    personas: list[dict], n: int, seed: str
) -> list[tuple[dict, str, int]]:
    """Repeat/cycle personas to reach N; alternate A/B after shuffle."""
    rng = stable_rng(seed)
    pool = list(personas)
    rng.shuffle(pool)
    assignments: list[tuple[dict, str, int]] = []
    i = 0
    while len(assignments) < n:
        p = pool[i % len(pool)]
        # block-ish alternate after shuffle of indices
        variant = "A" if len(assignments) % 2 == 0 else "B"
        # re-balance with rng for non-trivial mix while staying ~1:1
        if len(assignments) >= 2 and rng.random() < 0.0:
            pass
        assignments.append((p, variant, i))
        i += 1
    # final shuffle of assignment order but keep pairs roughly balanced
    rng.shuffle(assignments)
    # re-assign variants 1:1 after shuffle for strict between-subject balance
    balanced = []
    for idx, (p, _, offset) in enumerate(sorted(assignments, key=lambda t: t[2])):
        balanced.append((p, "A" if idx % 2 == 0 else "B", offset))
    rng.shuffle(balanced)
    return balanced[:n]


def mock_outcome(persona: dict, variant: str, seed: str, offset: int) -> dict:
    """Deterministic mock: B (benefit) slightly higher success; high price_sens harder on A."""
    rng = stable_rng(f"{seed}:{persona['id']}:{variant}:{offset}")
    sens = persona.get("price_sensitivity", "medium")
    base = 0.42 if variant == "A" else 0.55
    if sens == "high":
        base += -0.08 if variant == "A" else 0.04
    elif sens == "low":
        base += 0.06 if variant == "B" else 0.02
    success = rng.random() < base
    themes_a = ["непонятная цена", "CTA без обмена", "похоже на налог", "лучше Notes"]
    themes_b = ["понятен лимит", "цена на виду", "готов попробовать", "раздражает paywall рано"]
    themes = rng.sample(themes_a if variant == "A" else themes_b, k=min(2, 4))
    if not success and variant == "A":
        themes = ["путаница в тарифе", "Продолжить без цены"][:2]
    text = (
        f"# Raw · {persona['id']} · {variant}\n\n"
        f"Persona: {persona.get('display_name')} ({persona.get('segment')})\n"
        f"JTBD: {persona.get('jtbd')}\n\n"
        f"Mode: mock\nSuccess: {success}\nThemes: {', '.join(themes)}\n"
    )
    return {
        "success": success,
        "outcome": "success" if success else "reject_or_confused",
        "themes": themes,
        "raw": text,
        "model": "mock",
    }


def llm_outcome(persona: dict, variant: str, artifact: str, seed: str) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise SystemExit("SUL_RUNNER_MODE=llm requires OPENAI_API_KEY")
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    system = (
        "Ты синтетический пользователь в between-subject претесте. "
        "Видишь только один вариант лендинга. Ответь JSON: "
        '{"success": bool, "themes": [str,str], "note": str}. '
        "success=true если понятен обмен ценность/цена и есть intent или осознанный отказ по ценности. "
        "success=false если путаница, раздражение CTA, уход в Notes без понимания оффера."
    )
    user = (
        f"seed={seed}\npersona={json.dumps(persona, ensure_ascii=False)}\n"
        f"variant={variant}\nartifact:\n{artifact}\n"
    )
    body = {
        "model": model,
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "response_format": {"type": "json_object"},
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        content = payload["choices"][0]["message"]["content"]
        parsed = json.loads(content)
    except (urllib.error.URLError, KeyError, json.JSONDecodeError) as e:
        return {
            "success": False,
            "outcome": "llm_error",
            "themes": ["llm_error"],
            "raw": f"# LLM error\n{e}\n",
            "model": model,
        }
    success = bool(parsed.get("success"))
    themes = list(parsed.get("themes") or ["(none)"])[:3]
    note = parsed.get("note", "")
    raw = (
        f"# Raw · {persona['id']} · {variant}\n\nMode: llm ({model})\n"
        f"Success: {success}\nThemes: {', '.join(themes)}\nNote: {note}\n"
    )
    return {
        "success": success,
        "outcome": "success" if success else "reject_or_confused",
        "themes": themes,
        "raw": raw,
        "model": model,
    }


def write_protocol(out: Path, meta: dict) -> None:
    text = f"""# PROTOCOL (auto-filled by pretest_runner)

- Hypothesis: {meta['hypothesis_id']}
- Design: between-subject
- N: {meta['n']}
- Seed: `{meta['seed']}`
- Mode: {meta['mode']}
- Variants: A={meta['label_a']} · B={meta['label_b']}
- Primary: {meta['primary_metric']}
- Generated: {meta['generated']}

Boundaries: synthetic users are biased; direction match with live traffic is not proven a priori.
"""
    (out / "PROTOCOL.md").write_text(text, encoding="utf-8")


def write_report(out: Path, meta: dict, rows: list[dict]) -> None:
    by_v: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_v[r["variant"]].append(r)

    def rate(v: str) -> tuple[int, int, float]:
        xs = by_v.get(v, [])
        s = sum(1 for x in xs if x["success"] == "true" or x["success"] is True or x["success"] == True)
        # csv stores strings
        s = sum(1 for x in xs if str(x["success"]).lower() == "true")
        n = len(xs)
        return s, n, (s / n if n else 0.0)

    sa, na, ra = rate("A")
    sb, nb, rb = rate("B")
    theme_c: dict[str, Counter] = {"A": Counter(), "B": Counter()}
    for r in rows:
        for t in r["themes"].split("|"):
            if t:
                theme_c[r["variant"]][t] += 1

    def top(v: str) -> str:
        return ", ".join(f"{t} ({c})" for t, c in theme_c[v].most_common(5)) or "—"

    delta = rb - ra
    if abs(delta) < 0.05:
        verdict = "inconclusive"
    elif delta > 0:
        verdict = "supports (B direction)"
    else:
        verdict = "rejects (B weaker)"

    report = f"""# REPORT · {meta['hypothesis_id']} · N={meta['n']}

## 1. Дизайн и N

- between-subject, seed `{meta['seed']}`, mode `{meta['mode']}`
- N={meta['n']} · A={na} · B={nb}
- Artifact: лендинг/paywall copy Ритма (demo)

## 2. Метрики

| Variant | Success | N | Rate |
|---|---|---|---|
| A ({meta['label_a']}) | {sa} | {na} | {ra:.1%} |
| B ({meta['label_b']}) | {sb} | {nb} | {rb:.1%} |
| Δ (B−A) | | | {delta:+.1%} |

Primary = success_rate proxy (не живой pay). p-value не считаем — это претест.

## 3. Themes

- **A:** {top('A')}
- **B:** {top('B')}

## 4. Validity / смещения

- Синтетика смещена к «осознанности» и связным отказам.
- Артефакт = текст, не живой UI / App Store.
- Mock mode усиливает заданный эффект benefit-copy — для демо runner’а.
- Between-subject соблюдён: один variant на агента.

## 5. Вердикт + цена ошибки

**Вердикт:** {verdict}

Цена ошибки ship по синтетике: зря потраченный медиа-бюджет или упущенный живой тест онбординга/depth.

## 6. Следующий живой шаг

2 недели живого теста креатива/benefit-copy на реальном трафике после калибровки метрик depth.

---
_Generated by sul/runners/pretest_runner.py at {meta['generated']}_
"""
    (out / "REPORT.md").write_text(report, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="SUL S4 pretest runner (mock or llm)")
    ap.add_argument("--n", type=int, default=60)
    ap.add_argument("--seed", type=str, default="ritm-h02-20260918")
    ap.add_argument("--out", type=str, default="runs/demo-h02-landing-n60")
    ap.add_argument("--personas", type=str, default=str(DEFAULT_PERSONAS))
    ap.add_argument("--variants", type=str, default=str(DEFAULT_VARIANTS))
    ap.add_argument("--hypothesis", type=str, default="")
    args = ap.parse_args()

    mode = os.environ.get("SUL_RUNNER_MODE", "mock").lower()
    personas = load_personas(Path(args.personas))
    variants_doc = load_variants(Path(args.variants))
    hid = args.hypothesis or variants_doc.get("hypothesis_id", "H__")
    variants = variants_doc["variants"]

    out = Path(args.out)
    if not out.is_absolute():
        out = ROOT / out
    raw_dir = out / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    assignments = assign_between_subject(personas, args.n, args.seed)
    rows: list[dict] = []

    for persona, variant, offset in assignments:
        artifact = variants[variant]["artifact_text"]
        if mode == "llm":
            result = llm_outcome(persona, variant, artifact, args.seed)
        else:
            result = mock_outcome(persona, variant, args.seed, offset)
        raw_path = raw_dir / f"{persona['id']}_{variant}.md"
        # avoid overwrite when persona reused: include offset
        raw_path = raw_dir / f"{persona['id']}_{variant}_{offset}.md"
        raw_path.write_text(result["raw"], encoding="utf-8")
        rows.append(
            {
                "persona_id": persona["id"],
                "segment": persona.get("segment", ""),
                "variant": variant,
                "seed": args.seed,
                "model": result["model"],
                "outcome": result["outcome"],
                "success": str(bool(result["success"])).lower(),
                "themes": "|".join(result["themes"]),
                "path_raw": str(raw_path.relative_to(out)),
            }
        )

    meta = {
        "hypothesis_id": hid,
        "n": args.n,
        "seed": args.seed,
        "mode": mode,
        "label_a": variants["A"]["label"],
        "label_b": variants["B"]["label"],
        "primary_metric": variants_doc.get("primary_metric", "success_rate"),
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
    }
    write_protocol(out, meta)

    fields = [
        "persona_id",
        "segment",
        "variant",
        "seed",
        "model",
        "outcome",
        "success",
        "themes",
        "path_raw",
    ]
    with (out / "ASSIGNMENTS.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    with (out / "aggregate.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    write_report(out, meta, rows)
    print(f"Wrote {out} ({args.n} agents, mode={mode})")


if __name__ == "__main__":
    main()
