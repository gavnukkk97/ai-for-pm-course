# Материалы по модулям (reading list + gaps)

Индекс для производства и для студентов. База внешних ссылок: [`../external-materials.md`](../external-materials.md). Снапшоты: [`../materials-snapshots/`](../materials-snapshots/).

Легенда статусов gap: **filled** · **thin** · **todo**.

---

## Н0 — Онбординг

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| Docs | [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart) · snapshot [`claude-code-quickstart.md`](../materials-snapshots/claude-code-quickstart.md) | если выбран Claude Code | filled |
| Docs | Cursor install + Agent chat (сайт Cursor) | если выбран Cursor | filled (link) |
| Docs | [Choose how to use n8n](https://docs.n8n.io/choose-how-to-use-n8n/) · snapshot | да | filled |
| Docs | [n8n Docker install](https://docs.n8n.io/hosting/installation/docker/) · snapshot extract | local path | filled |
| Prior course | `product-analytics-ai-course` → student-getting-started / stand (тур Ритм) | instructor | filled |
| YT | [6 способов AI для PM](https://www.youtube.com/watch?v=ET3z8wSNUiA) | опц. | filled |
| YT | [AI-Native PM webinar](https://www.youtube.com/watch?v=Xp_iIkt94TQ) | опц. | filled |
| Paid | LI Learning Marily Nika — AI Agents for Product Leaders | опц. | thin (paid) |

**Gaps:** короткий RU-скринкаст «ставим Cursor за 10 мин» своим автором — **todo**.

Студенческие тексты: [`week-00/`](./week-00/).

---

## Н1 — Экзоскелет + n8n + S0

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| Docs | [Cursor Skills](https://cursor.com/docs/skills) · snapshot | Cursor track | filled |
| Docs | [Claude Code custom skills](https://code.claude.com/docs/en/custom-skills) · snapshot | Claude track | filled |
| Spec | [Agent Skills specification](https://agentskills.io/specification) · snapshot | опц. | filled |
| Docs | [MCP intro](https://modelcontextprotocol.io/docs/getting-started/intro) · snapshot | skim | filled |
| GitHub | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) · README snapshot | выборочно | filled |
| GitHub | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) · snapshot | альт. библиотека | filled |
| Medium | [Why PM care about Agent Harness](https://medium.com/design-bootcamp/why-should-pm-care-about-agent-harness-5e4a5ae5a1ee) | пересказ на занятии | thin (no full dump) |
| YT | [Claude for PMs](https://www.youtube.com/watch?v=bITUsUsrxjM) | реком. | filled |
| YT | [Why Every PM Must Use Claude Code](https://www.youtube.com/watch?v=hLYK28IlvyE) | опц. | filled |
| Docs | [n8n AI intro tutorial](https://docs.n8n.io/advanced-ai/intro-tutorial/) | да | filled (link; extract noisy) |
| Docs | [Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) · snapshot | да | filled |
| Docs | [Read/Write Files](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/) · snapshot | self-hosted | filled |
| Blog | [n8n: AI Agents Explained](https://blog.n8n.io/ai-agents/) · excerpt snapshot | опц. | filled |
| GitHub | [n8n-io/skills TOOLS ref](https://github.com/n8n-io/skills) · snapshot | instructor | filled |
| Paper | AgentA/B abstract + PDF | границы SUL | filled |
| Our | [`sul/`](./sul/) S0 kit · [`week-01/`](./week-01/) | да | filled |

**Gaps:** MCP hands-on lab (Linear/Notion) — **todo** (Н1 достаточно intro).

Студенческие тексты: [`week-01/`](./week-01/).

---

## Н2 — ICP / конкуренты / УТП → банк персон (S1 старт)

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| Medium | Discovery agent stack (Gottlob) | пересказ | thin |
| GitHub | [pm-skills](https://github.com/phuryn/pm-skills) market-research | skim | filled (link) |
| YT | [Building synthetic users…](https://www.youtube.com/watch?v=b4MUT_NSq7M) | 1 из 2 YT | filled |
| YT | [What are Synthetic Users?](https://www.youtube.com/watch?v=w-bZckedky8) | альт. | filled |
| Our | [`sul/personas/persona.schema.json`](./sul/personas/persona.schema.json) + example | да | filled |
| Our | [`sul/personas/persona-bank-guide.md`](./sul/personas/persona-bank-guide.md) (**S1**) | да | filled |
| Our | [`week-02/`](./week-02/) pack | да | filled |
| SaaS ref | syntheticusers.com (сравнение, не зависимость) | опц. | filled |

**Gaps:** эталон ICP «Ритм» — **filled** ([`instructor/rhythm-exemplars/01-icp-competitive-map.md`](./instructor/rhythm-exemplars/01-icp-competitive-map.md)). Карта конкурентов — **filled**.

**Required readings (студент):** schema + bank guide · 1 YT synthetic users · pm-skills market-research skim.

---

## Н3 — Discovery + упаковка (Минто) → S2

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| GitHub | [voice-of-agents](https://github.com/blakeaber/voice-of-agents) · README snapshot | ethics | filled |
| YT | [6 способов AI…](https://www.youtube.com/watch?v=ET3z8wSNUiA) | опц. | filled |
| YT | [Feedback from synthetic users](https://www.youtube.com/watch?v=q_fdcbwHJKQ) | опц. | filled |
| Prior | stats-ab 4.6 AgentA/B (between-subject) | да (конспект) | filled |
| Our | [`sul/hypotheses/_TEMPLATE.md`](./sul/hypotheses/_TEMPLATE.md) | да | filled |
| Our | [`sul/hypotheses/hypothesis-runner-stub.md`](./sul/hypotheses/hypothesis-runner-stub.md) (**S2**) | да | filled |
| Our | [`week-03/`](./week-03/) pack · n8n flow #2 | да | filled |
| Our | [`sul/n8n/flow-02-signals-to-digest.json`](./sul/n8n/flow-02-signals-to-digest.json) + description | да | filled |
| Our | [`instructor/rhythm-exemplars/02-discovery-brief.md`](./instructor/rhythm-exemplars/02-discovery-brief.md) | instructor | filled |

**Gaps:** отдельный файл red-team checklist (сейчас в brief + REDTEAM.md задание) — **thin**.

**Required readings:** voice-of-agents README · hypothesis template + runner stub · AgentA/B between-subject reminder.

---

## Н4 — AI-ставки / стратегия → S3

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| arXiv | [SSR purchase intent](https://arxiv.org/abs/2510.08338) · PDF snapshot | abstract | filled |
| GitHub | [synthetic-market-research](https://github.com/BayramAnnakov/synthetic-market-research) | README | filled |
| GitHub | [semantic-similarity-rating](https://github.com/pymc-labs/semantic-similarity-rating) | опц. | filled |
| YT RU | [ИИ-агенты как продукт](https://www.youtube.com/watch?v=Ieq8cY0UcHo) | опц. | filled |
| Our | [`sul/templates/market-tornado.md`](./sul/templates/market-tornado.md) (**S3**) | да | filled |
| Our | [`sul/templates/decision-memo-stub.md`](./sul/templates/decision-memo-stub.md) | да | filled |
| Our | [`week-04/`](./week-04/) pack | да | filled |
| Our | [`instructor/rhythm-exemplars/03-strategy-go-no-go-memo.md`](./instructor/rhythm-exemplars/03-strategy-go-no-go-memo.md) | instructor | filled |

**Gaps:** P0 strategy/tornado эталон — **filled**.

**Required readings:** SSR abstract · synthetic-market-research README · market-tornado template.

---

## Н5 — Дерево метрик / юнит / финмодель

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| Prior | `itmo-product-analytics` шпаргалки метрик/юнита | да | filled (repo) |
| Prior | Ритм М1.3 unit economics | instructor pattern | filled (repo) |
| GitHub | pm-skills analytics | skim | filled (link) |
| Our | [`week-05/`](./week-05/) pack (DEFINITIONS / tree / scenarios) | да | filled |
| Our | [`instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md`](./instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md) | instructor | filled |

**Gaps:** spreadsheet `.xlsx` шаблон 3 сценария — **todo** (P2; MD-таблица в brief + эталон markdown — **filled**).

**Required readings:** week-05 brief · шпаргалка метрик из prior course · калибровочный ритуал.

---

## Н6 — Аналитика bare vs rich → S4 старт

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| Medium | AI Agents for PMs | пересказ | thin |
| Prior | Ритм PRODUCT_CONTEXT / data dictionary | pattern | filled (repo) |
| Our | n8n flow #3 [`sul/n8n/flow-03-analytics-digest.json`](./sul/n8n/flow-03-analytics-digest.json) | да | filled |
| Our | [`sul/templates/pretest-protocol.md`](./sul/templates/pretest-protocol.md) (**S4** design) | да | filled |
| Our | [`instructor/rhythm-exemplars/05-bare-vs-rich-context-pack.md`](./instructor/rhythm-exemplars/05-bare-vs-rich-context-pack.md) | instructor | filled |
| Our | [`week-06/`](./week-06/) pack | да | filled |

**Gaps:** P0 rich-pack outline + flow #3 JSON — **filled**.

**Required readings:** pretest protocol · week-06 bare vs rich exercise · AgentA/B abstract refresh.

---

## Н7 — Коммуникации + претест S4

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| arXiv | [AgentA/B](https://arxiv.org/abs/2504.09723) · [SimAB](https://arxiv.org/abs/2603.01024) | да | filled |
| GitHub | pm-skills GTM | skim | filled (link) |
| Prior | stats-ab 4.6 практика персон | да | filled |
| Our | pretest protocol + [`week-07/`](./week-07/) pack | да | filled |
| Our | [`sul/runners/`](./sul/runners/) + sample [`runs/demo-h02-landing-n60/REPORT.md`](./sul/runners/runs/demo-h02-landing-n60/REPORT.md) | да | filled |
| Our | [`instructor/rhythm-exemplars/06-pretest-pitch-demo-notes.md`](./instructor/rhythm-exemplars/06-pretest-pitch-demo-notes.md) | instructor | filled |

**Gaps:** sample REPORT N=60 + runner — **filled**. Питч-дек каркас отдельным `pitch-outline.md` — **thin** (секции в brief + demo notes).

**Required readings:** AgentA/B · pretest protocol · week-07 brief (питч + S4).

---

## Н8 — Капстоун S5

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| Our | [`sul/validity-rubric-stub.md`](./sul/validity-rubric-stub.md) | да | filled |
| Our | [`sul/templates/s5-defense-rubric.md`](./sul/templates/s5-defense-rubric.md) (**S5**) | да | filled |
| Our | [`week-08/`](./week-08/) pack | да | filled |
| Paper | AgentA/B + SimAB калибровка | да | filled |

**Gaps:** talk-track защиты — **filled** (в [`06-pretest-pitch-demo-notes.md`](./instructor/rhythm-exemplars/06-pretest-pitch-demo-notes.md)). Заполненный sample RUBRIC на Ритм — **todo** (P2). Playbook 0–8 — **filled** ([`instructor/playbook-0-8.md`](./instructor/playbook-0-8.md)).

**Required readings:** s5-defense-rubric · свой S4 REPORT · calibration notes.

---

## Instructor pack (сквозное)

| Материал | Path | Gap |
|---|---|---|
| Playbook Н0–Н8 | [`instructor/playbook-0-8.md`](./instructor/playbook-0-8.md) | filled |
| Rhythm exemplars | [`instructor/rhythm-exemplars/`](./instructor/rhythm-exemplars/) | filled |
| Local push brief (kir) | [`../local-push-brief.md`](../local-push-brief.md) | filled |

---

## Private ops (не студентам)

Mail.ru / Яндекс шары — только авторы/kir; паттерны переписывать в наши тексты. Список в программе §4.3.
