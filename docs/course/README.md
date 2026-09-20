# Материалы курса «AI для продакта»

Студенческая выдача. Программа зафиксирована в [`../ai-for-pm-course-program.md`](../ai-for-pm-course-program.md) — **не переписываем сетку**, только наполняем практику.

**Одна фраза:** прошлые курсы учат *считать*; этот — *собрать AI-контур продакта* (harness + n8n) и **Synthetic User Lab** на своём продукте. Демо преподавателей — на стенде **Ритм**.

---

## Карта папки → 8 недель + SUL

| Папка | Неделя / веха | Статус производства |
|---|---|---|
| [`week-00/`](./week-00/) | **Н0** async-онбординг: env, LLM, договор «AI ≠ вывод», 1-pager своего продукта | draft v1 |
| [`week-01/`](./week-01/) | **Н1** AI-экзоскелет: fluency ≥1 harness, skill, n8n flow #1, **S0** | draft v1 |
| [`week-02/`](./week-02/) | **Н2** ICP / конкуренты / УТП → банк персон (**S1** старт) | draft v1 |
| [`week-03/`](./week-03/) | **Н3** Discovery + Минто → гипотезы, digest, **S2** старт | draft v1 |
| [`week-04/`](./week-04/) | **Н4** AI-ставки / стратегия → sizing + tornado (**S3**) | draft v1 |
| [`week-05/`](./week-05/) | **Н5** Дерево метрик / юнит / 3 сценария | draft v1 |
| [`week-06/`](./week-06/) | **Н6** Bare vs rich аналитика → **S4** старт (protocol) | draft v1 |
| [`week-07/`](./week-07/) | **Н7** Питч + претест ≥50–100 (**S4**) | draft v1 |
| [`week-08/`](./week-08/) | **Н8** Капстоун / защита (**S5**) | draft v1 |
| [`sul/`](./sul/) | Флагман **S0→S5**: scaffold + шаблоны S1–S5 + n8n #1–#3 + S4 runner | draft v2 |
| [`instructor/`](./instructor/) | Playbook 0–8 + **эталоны Ритм** | v2 |
| [`materials-by-module.md`](./materials-by-module.md) | Reading list + gaps по каждой неделе | живой индекс |

Внешние источники и снапшоты: [`../external-materials.md`](../external-materials.md), [`../materials-snapshots/`](../materials-snapshots/).

**Instructor pack (v2):** [`instructor/playbook-0-8.md`](./instructor/playbook-0-8.md) · [`instructor/rhythm-exemplars/`](./instructor/rhythm-exemplars/) · n8n [`sul/n8n/`](./sul/n8n/) · runner [`sul/runners/`](./sul/runners/).  
Локальный синк в GitHub: [`../local-push-brief.md`](../local-push-brief.md).

---

## Что в каждой недельной папке

Ориентир тона — уроки «Ритм» (`product-analytics-ai-course`) и AgentA/B (`stats-ab-course` 4.6): коротко, с критериями приёмки, без воды.

| Файл | Для кого | Содержание |
|---|---|---|
| `lesson-outline.md` | преподаватель + студент | цели, тайминг, теория-скелет, практика, mermaid |
| `student-brief.md` | студент | что сделать за неделю, артефакты, как сдавать |
| `instructor-notes.md` | преподаватель | демо на **Ритме**, типичные сбои, что не показывать |
| `checklist.md` | оба | приёмка недели |

---

## Сквозные артефакты студента

1. **Свой продукт / рабочий кейс** — 1-pager с Н0, все гипотезы и SUL на нём.  
2. **Harness** — Cursor *или* Claude Code (≥1 свободно).  
3. **n8n** — local или cloud; с Н1 — рабочий flow #1 (+ digests на Н3/Н6).  
4. **SUL-репо** — структура из [`sul/`](./sul/) под свой продукт, вехи S0→S5.

Преподаватели параллельно гоняют тот же конвейер на Ритме (эталон, не замена кейса студента).

---

## Анти-скоуп (напоминание)

- не повтор JTBD / юнит / АБ «с нуля»;  
- n8n ≠ курс автопостинга;  
- облака Mail.ru / Яндекс — **не** в студенческой выдаче;  
- синтетика ≠ живой трафик (слайд границ на каждой SUL-вехе).

---

## Дальше по производству

v2 P0/P1 gaps (эталоны Ритм, n8n #2/#3, S4 runner, playbook) — **закрыты**. Остаётся P2 (скринкаст Cursor, `.xlsx` Н5, sample RUBRIC) и локальный push — см. [`../local-push-brief.md`](../local-push-brief.md), [`../../internal/materials-production.md`](../../internal/materials-production.md).
