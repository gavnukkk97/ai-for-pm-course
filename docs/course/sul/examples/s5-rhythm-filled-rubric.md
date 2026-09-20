# EXAMPLE · S5 filled rubric · Ритм (не студенческая сдача)

> **EXAMPLE / instructor calibration only.**  
> Продукт: учебный стенд **Ритм**. Не принимать как кейс студента.  
> Опора: [`../runners/runs/demo-h02-landing-n60/REPORT.md`](../runners/runs/demo-h02-landing-n60/REPORT.md) · эталоны [`../../instructor/rhythm-exemplars/`](../../instructor/rhythm-exemplars/).

Шаблон: [`../templates/s5-defense-rubric.md`](../templates/s5-defense-rubric.md).  
Шкала: `0` нет · `1` слабо · `2` достаточно · `3` сильно.

**Оценщик (демо):** Instructor · **Дата:** 2026-09-18 · **Run:** `demo-h02-landing-n60`

---

## A. Дизайн симуляции (max 15)

| # | Критерий | Балл | Комментарий |
|---|---|---|---|
| A1 | Гипотеза X→Y→Z, метрика до прогона | **3** | H02: benefit-copy → intent/pay proxy; Z в protocol до run |
| A2 | Between-subject, без утечки | **3** | Один variant на агента; ASSIGNMENTS.csv |
| A3 | N ≥ 50 | **3** | N=60 (A30/B30) |
| A4 | Seed / модель / temperature | **2** | Seed `ritm-h02-20260918`; mock mode — temperature N/A, зафиксирован mode |
| A5 | Артефакт = тип живого | **2** | Текст лендинга/paywall; не App Store UI — отмечено в validity |

**A = 13 / 15**

## B. Персоны и рынок (max 12)

| # | Критерий | Балл | Комментарий |
|---|---|---|---|
| B1 | ≥15 персон, ≥3 сегмента | **3** | Эталон банка (freelance / parents / maxers) |
| B2 | Sources не только llm_draft | **2** | Mix desk + analytics_cluster + interview notes (демо) |
| B3 | S3 sizing + tornado | **2** | [`03-strategy-go-no-go-memo.md`](../../instructor/rhythm-exemplars/03-strategy-go-no-go-memo.md) |
| B4 | Ставки ↔ гипотезы | **3** | Thin-bet pretest H02 до медиа |

**B = 10 / 12**

## C. Внешняя валидность (max 12)

| # | Критерий | Балл | Комментарий |
|---|---|---|---|
| C1 | Калибровка или calibration debt | **2** | Debt явный: mock усиливает benefit-эффект; нет живого АБ того же креатива |
| C2 | WHERE-IT-LIES конкретно | **3** | SSR/intent ≠ purchase; текст≠UI; mock bias |
| C3 | Цена ошибки | **3** | Медиа-бюджет / упущенный тест онбординга |
| C4 | Вердикт согласован с данными | **3** | supports (B); Δ +20pp; не ship без живого |

**C = 11 / 12**

## D. Коммуникация и процесс (max 12)

| # | Критерий | Балл | Комментарий |
|---|---|---|---|
| D1 | «Не доказали» + ask | **3** | Питч + memo: не доказали purchase; ask = 2 нед. живого теста |
| D2 | SUL README статусы S0–S5 | **2** | Демо-репо; статусы в playbook/exemplars |
| D3 | n8n + harness следы | **2** | Flow #1–#3 + runner в sul/; не только чат |
| D4 | Peer-review заполнен | **2** | Ниже — учебный peer (instructor↔TA) |

**D = 9 / 12**

**Сумма: 43 / 51** → ориентир «сильная защита» (≥36). Авто-fail: нет.

---

## Обязательный абзац (заполненный)

> По симуляции мы бы: **приоритизировали benefit-copy (B) для следующего живого креатива и не крутили цену первой**.  
> Этого **недостаточно**, чтобы: **ship paywall в прод или закупать медиа на полном бюджете**.  
> Следующий живой шаг: **2 недели A/B креатива/benefit на реальном трафике + замер depth≥3 как product NS**.

---

## Авто-fail

- [ ] ship/kill при 0 в C — нет  
- [ ] нет REPORT / N<50 — нет (REPORT + N=60)  
- [ ] API keys в git — нет  
- [ ] Ритм сдан как «свой продукт» — **N/A (это EXAMPLE instructor)**  
- [ ] within-subject — нет  

---

## Peer-review (учебный)

| Вопрос | Да/нет + комментарий |
|---|---|
| Primary metric за 30 сек? | Да — success_rate proxy A vs B |
| Чего не доказали? | Да — purchase / App Store CV |
| Вердикт честный? | Да — supports direction, не «победили рынок» |
| Риск смещения? | Mock mode раздувает Δ |
| Совет по живому шагу? | Сначала креатив/онбординг, не price A/B |

Рецензент: TA (demo) · Дата: 2026-09-18

---

## Как пользоваться на оценке

1. Покажите класссу **этот** EXAMPLE рядом с пустым шаблоном.  
2. Сверьте баллы с артефактами в `runs/demo-h02-landing-n60/` — не с «красотой слайдов».  
3. Студенческий кейс на Ритме как продукте = **авто-fail** (см. рубрику).
