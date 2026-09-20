# Эталон · Bare vs rich context pack · Ритм

**Неделя:** Н6 · instructor demo  
Студенты собирают `context/` на **своём** продукте; ниже — outline эталона Ритма.

---

## Вопрос демо

«Почему paywall conversion просел на прошлой неделе?»

---

## Bare (ожидаемый провал)

**Вход:** только вопрос + короткая таблица без словаря:

| week | paywall_views | pays |
|---|---|---|
| W-2 | 420 | 38 |
| W-1 | 410 | 36 |
| W0 | 405 | 22 |

**Типичные галлюцинации агента (показать классу):**

- «баг iOS 18» — в таблице нет `platform`  
- «выросла цена» — цены в входе нет  
- «сезонность августа» — без календаря релизов  

Сохранить как `analysis/bare.md` в демо-репо.

---

## Rich pack outline (`context/`)

### `PRODUCT_CONTEXT.md` (сжато)

- Ритм: habit freemium→Pro; JTBD 1–3 ритуала; NSM D7 depth≥3.  
- Сегменты: habit-starters-freelance / relapse-parents / productivity-maxers.  
- Табуированные выдумки: не выдумывать события вне tracking; не считать CAC без DEFINITIONS; не ship по синтетике.

### `data-dictionary.md` (поля заглушки)

| Field | Meaning | Join |
|---|---|---|
| user_id | пользователь | PK |
| event_name | install, onboarding_completed, habit_created, check_in, paywall_view, subscribe | |
| ts | UTC timestamp | |
| platform | ios / android / web | optional |
| experiment_id | напр. paywall_timing_2026q3 | |
| variant | control / treatment | |

### `pitfalls.md` (≥5)

1. Путает retention D7 и depth≥3.  
2. Склеивает недели до/после релиза онбординга.  
3. Выдумывает platform split.  
4. ARPU вместо ARPPU на freemium.  
5. Early paywall share игнорирует как guardrail.  
6. LLM-оптимизм «достаточно снизить цену».

### `links.md`

- `metrics/DEFINITIONS.md` ← эталон дерева Н5  
- `research/icp-ritm.md` ← эталон Н2  
- `hypotheses/H02-*.md`  
- `sul/SYNTHETIC-DATA-NOTICE.md`

### CSV-заглушка событий

Достаточно Markdown-таблицы на занятии (не prod Metabase credentials):

| user_id | event_name | ts | note |
|---|---|---|---|
| u1 | habit_created | W0-3d | |
| u1 | paywall_view | W0-2d | early |
| … | onboarding_release | W0 start | **релиз** укороченного онбординга |

Человек-калибровка: «недели несравнимы — релиз онбординга».

---

## COMPARE.md (5 строк эталон)

1. Bare выдумал iOS-баг.  
2. Rich потребовал dictionary → отказался от platform.  
3. Rich предложил проверить overlap с релизом онбординга.  
4. Оба не знают креатив канала — дыра.  
5. Вердикт человека: расследование релиза + guardrail early PW; не крутить цену.

---

## n8n flow #3

Schedule → read STATUS/metrics snippet → LLM summary → `runs/n8n/digest-metrics-<date>.md`.  
Import: `sul/n8n/flow-03-analytics-digest.json`.
