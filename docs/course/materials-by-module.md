# Материалы по модулям (reading list + gaps)

Индекс для производства и для студентов. База внешних ссылок: [`../external-materials.md`](../external-materials.md). Офлайн-снапшоты в публичный репозиторий не входят — см. URL в [`../external-materials.md`](../external-materials.md).

Легенда статусов gap: **filled** · **thin** · **todo**.

---

## Н0 — Онбординг

| Тип | Материал | Обязательность | Gap |
|---|---|---|---|
| Docs | [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart) | если выбран Claude Code | filled |
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

**Gaps:** MCP hands-on lab (Linear/Notion) — **todo** (Н1 достаточно intro). Полный instructor playbook Н2–8 — **todo**.

---

## Н2 — ICP / конкуренты / УТП → банк персон (S1 старт)

| Тип | Материал | Gap |
|---|---|---|
| Medium | Discovery agent stack (Gottlob) | thin |
| GitHub | pm-skills market-research plugin | filled (link) |
| YT | [Building synthetic users…](https://www.youtube.com/watch?v=b4MUT_NSq7M) | filled |
| YT | [What are Synthetic Users?](https://www.youtube.com/watch?v=w-bZckedky8) | filled |
| Our | persona schema + example в `sul/personas/` | filled |
| SaaS ref | syntheticusers.com (сравнение, не зависимость) | filled |

**Gaps:** эталон ICP «Ритм» 2–3 стр. · студенческий brief Н2 · шаблон карты конкурентов — **todo**.

---

## Н3 — Discovery + упаковка (Минто) → S2

| Тип | Материал | Gap |
|---|---|---|
| GitHub | [voice-of-agents](https://github.com/blakeaber/voice-of-agents) · README snapshot | filled |
| YT | [6 способов AI…](https://www.youtube.com/watch?v=ET3z8wSNUiA) | filled |
| YT | [Feedback from synthetic users](https://www.youtube.com/watch?v=q_fdcbwHJKQ) | filled |
| Prior | stats-ab 4.6 AgentA/B (этика/between-subject) | filled |
| Our | `hypotheses/_TEMPLATE.md` | filled |

**Gaps:** red-team checklist отдельным файлом · n8n digest flow #2 · Мinto one-pager эталон — **todo**.

---

## Н4 — AI-ставки / стратегия → S3

| Тип | Материал | Gap |
|---|---|---|
| arXiv | [SSR purchase intent](https://arxiv.org/abs/2510.08338) · PDF snapshot | filled |
| GitHub | [synthetic-market-research](https://github.com/BayramAnnakov/synthetic-market-research) | filled |
| GitHub | [semantic-similarity-rating](https://github.com/pymc-labs/semantic-similarity-rating) | filled |
| YT RU | [ИИ-агенты как продукт](https://www.youtube.com/watch?v=Ieq8cY0UcHo) | filled |

**Gaps:** tornado-шаблон Excel/MD · strategy memo эталон на Ритме — **todo**.

---

## Н5 — Дерево метрик / юнит / финмодель

| Тип | Материал | Gap |
|---|---|---|
| Prior | `itmo-product-analytics` шпаргалки метрик/юнита | filled (repo) |
| Prior | Ритм М1.3 unit economics | filled (repo) |
| GitHub | pm-skills analytics | filled (link) |

**Gaps:** студенческий brief «агент считает — человек калибрует» · spreadsheet-шаблон 3 сценария — **todo**.

---

## Н6 — Аналитика bare vs rich → S4 старт

| Тип | Материал | Gap |
|---|---|---|
| Medium | AI Agents for PMs | thin |
| Prior | Ритм PRODUCT_CONTEXT / data dictionary | filled (repo) |
| Our | n8n schedule digests (ещё не описан flow #3) | todo |

**Gaps:** эталон rich-пакета · bare vs rich упражнение на Ритме — **todo**.

---

## Н7 — Коммуникации + претест S4

| Тип | Материал | Gap |
|---|---|---|
| arXiv | AgentA/B · SimAB PDFs | filled |
| GitHub | pm-skills GTM | filled (link) |
| Prior | stats-ab 4.6 практика персон | filled |

**Gaps:** протокол прогона ≥50–100 · шаблон отчёта симуляции · питч-дек каркас — **todo**.

---

## Н8 — Капстоун S5

| Тип | Материал | Gap |
|---|---|---|
| Our | [`sul/validity-rubric-stub.md`](./sul/validity-rubric-stub.md) | filled stub |
| Paper | AgentA/B + SimAB калибровка | filled |

**Gaps:** полная рубрика баллов · peer-review лист · эталон защиты Ритм — **todo**.

---

## Private ops (не студентам)

Mail.ru / Яндекс шары — только авторы/kir; паттерны переписывать в наши тексты. Список в программе §4.3.
