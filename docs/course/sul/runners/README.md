# S4 Pretest Runner (reference)

Reference implementation for [`../templates/pretest-protocol.md`](../templates/pretest-protocol.md).  
Between-subject A/B stub; seed for reproducibility; **mock by default**.

## Modes

| Mode | Env | Behavior |
|---|---|---|
| **mock** (default) | unset / `SUL_RUNNER_MODE=mock` | Deterministic outcomes from seed + persona + variant — no network |
| **llm** | `SUL_RUNNER_MODE=llm` + `OPENAI_API_KEY` | Optional chat completion; needs `openai` or stdlib+urllib |

Never commit API keys. Optional: `pip install openai` or use urllib against OpenAI-compatible API.

## Quick start

```bash
cd docs/course/sul/runners   # or your copy under sul-lab/runners

# Dry-run / demo N=60 (writes under runs/)
python3 pretest_runner.py --n 60 --seed ritm-h02-20260918 --out runs/demo-h02-landing-n60

# Smoke N=5
python3 pretest_runner.py --n 5 --seed smoke-001 --out runs/smoke-local

# LLM mode (optional)
export SUL_RUNNER_MODE=llm
export OPENAI_API_KEY=sk-...          # local only
export OPENAI_MODEL=gpt-4o-mini       # optional
python3 pretest_runner.py --n 6 --seed live-smoke --out runs/llm-smoke
```

Notebook twin: [`pretest_runner.ipynb`](./pretest_runner.ipynb) — same logic, step-by-step.

## Inputs

- `seed_data/personas.jsonl` — demo personas (Ритм segments; replace with yours)
- `seed_data/variants.json` — A/B artifact texts
- CLI: `--hypothesis H02`, `--n`, `--seed`, `--out`

## Outputs (`--out` dir)

```text
PROTOCOL.md       # filled stub
ASSIGNMENTS.csv
aggregate.csv
REPORT.md
raw/<persona>_<variant>.md
```

## Alignment with protocol

- Design: between-subject (one variant per agent)  
- No «choose better»  
- Seed required  
- REPORT sections: design, metrics, themes, validity, verdict, next live step  

## Dependencies

- **Required:** Python 3.10+ stdlib only (mock mode)  
- **Optional:** `openai` package *or* raw HTTPS via urllib when `SUL_RUNNER_MODE=llm`
