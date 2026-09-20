# Н6 · Student brief — rich-пакет, digests, старт S4

Практика **4–6 ч**. Сдача: `context/` pack + отчёт bare-vs-rich + flow #3 + черновик pretest protocol.

---

## A. Rich context pack

Соберите `context/`:

| Файл | Минимум |
|---|---|
| `PRODUCT_CONTEXT.md` | продукт, NS, сегменты, табуированные выдумки |
| `data-dictionary.md` | поля ваших выгрузок / событий |
| `pitfalls.md` | ≥5 «агент обычно врёт так» |
| `links.md` | пути к metrics/DEFINITIONS, ICP, гипотезам |

Скопируйте *паттерн* из Ритма (если видели на занятии), не содержимое.

---

## B. Упражнение bare vs rich

1. Выберите **один** вопрос (напр. «почему упала активация?»).  
2. **Bare:** агенту только вопрос + 1 CSV/таблица без словаря. Сохраните ответ `analysis/bare.md`.  
3. **Rich:** тот же вопрос + весь `context/`. Ответ `analysis/rich.md`.  
4. `analysis/COMPARE.md`: что выдумал bare; что rich исправил; что оба пропустили; ваш вердикт как человека.

---

## C. Два сценария анализа

В `analysis/scenarios/`:

1. Funnel snapshot (шаги, конверсии, окно).  
2. Feedback themes (если нет отзывов — desk + synthetic themes с меткой).

---

## D. n8n flow #3 — schedule digests

```
Schedule (напр. weekly)
  → Read metrics или STATUS / evidence
  → LLM summary
  → Write runs/n8n/digest-metrics-<date>.md
```

Задокументируйте cron/расписание в SUL README. На сдаче достаточно 1 ручного Execute с пометкой «schedule configured».

---

## E. S4 старт

Скопируйте [`../sul/templates/pretest-protocol.md`](../sul/templates/pretest-protocol.md) → `runs/pretest/PROTOCOL-<H__.md>`.

Заполните дизайн: гипотеза, A/B, N целевое 50–100, seed, artifact URL **своего** продукта, success event = Z.  
Прогон на полном N — на Н7; сейчас достаточно dry-run на 3–5 агентах (опционально) с логом в `runs/pretest/smoke/`.

---

## F. Чтение

Ритм context pattern · Medium AI Agents for PMs (пересказ на занятии) · AgentA/B abstract refresh.

---

## Критерии

[`checklist.md`](./checklist.md).
