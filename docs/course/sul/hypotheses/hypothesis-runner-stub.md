# S2 · Hypothesis runner stub

Скопируйте этот файл в `hypotheses/runners/H0N-plan.md` и заполните **до** любого массового прогона.

Связанный шаблон гипотезы: [`_TEMPLATE.md`](./_TEMPLATE.md).

Недели: старт **Н3**, дожим **Н4**.

---

## Мета

| Поле | Значение |
|---|---|
| Hypothesis id | H__ |
| Run plan id | RP-__ |
| Owner | |
| Created | |
| Status | draft / ready / blocked |

---

## Входы (должны существовать на диске)

- [ ] Файл гипотезы с X→Y→Z без дыр в Z  
- [ ] Список persona ids (или правило сэмпла из сегментов)  
- [ ] Artifact A path/URL  
- [ ] Artifact B path/URL  
- [ ] Success event = Z  
- [ ] Guardrail metric (опц.)

---

## План сэмпла

| Параметр | Значение |
|---|---|
| Design | **between-subject** (курс default) |
| N total | |
| N per variant | |
| Stratify by segment? | yes/no — как |
| Seed | |
| Model | |
| Temperature | |
| Max steps / tokens per agent | |

---

## Алгоритм (псевдо)

```text
1. load personas (filter by ids/segments)
2. shuffle with seed
3. assign variant A|B alternating or block-random
4. for each agent:
     - build prompt: persona + ONE variant only + task
     - run until success_signal | give_up | max_steps
     - record: persona_id, variant, outcome, themes, raw_path
5. aggregate: conversion, WTP-proxy, theme counts
6. write runs/<run_id>/REPORT.md skeleton
```

Реализация: ноутбук / Python / n8n batch — на выбор. Этот stub = контракт.

---

## Метрики (заполнить формулы)

| Метрика | Формула | Primary? |
|---|---|---|
| | | yes/no |
| | | |

---

## Red-team runner-specific

1. Как промпт может утечь признаками варианта?  
2. Как stop-rule смещает outcome?  
3. …

---

## Выходы

```text
runs/<run_id>/
  ASSIGNMENTS.csv
  raw/
  aggregate.json
  REPORT.md
```

---

## Gate ready → run

- [ ] Все входы существуют  
- [ ] Between-subject подтверждён  
- [ ] Seed записан  
- [ ] Человек утвердил primary metric  
- [ ] SYNTHETIC-DATA-NOTICE учтён в REPORT шаблоне
