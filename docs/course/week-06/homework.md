# Н6 · Домашнее задание — rich-пакет, digests #3, дизайн S4

**Срок:** до занятия Н7.  
**Оценка часов:** **4–6 ч**.  
**Связанные файлы:** [`student-brief.md`](./student-brief.md) · [`checklist.md`](./checklist.md) · [`lecture.md`](./lecture.md)  
**SUL веха:** **S4 design** — [`../sul/templates/pretest-protocol.md`](../sul/templates/pretest-protocol.md) · n8n [`../sul/n8n/flow-03-description.md`](../sul/n8n/flow-03-description.md) · runner prep [`../sul/runners/README.md`](../sul/runners/README.md)

---

## Зачем

Собрать rich context pack, доказать ценность контекста (bare vs rich), поставить schedule-digest, **спроектировать** pretest (полный N — на Н7).

---

## Задачи

### A. Rich context pack (≈75–90 мин)

Папка `context/`:

| Файл | Минимум |
|---|---|
| `PRODUCT_CONTEXT.md` | продукт, NS, сегменты, табуированные выдумки |
| `data-dictionary.md` | поля выгрузок/событий |
| `pitfalls.md` | ≥5 «агент обычно врёт так» |
| `links.md` | пути к DEFINITIONS, ICP, гипотезам |

Паттерн — с занятия/эталона; **содержимое** — своё.

### B. Bare vs rich (≈60–90 мин)

1. Один аналитический вопрос (напр. «почему упала активация?»).  
2. **Bare:** вопрос + 1 таблица без словаря → `analysis/bare.md`.  
3. **Rich:** тот же вопрос + весь `context/` → `analysis/rich.md`.  
4. `analysis/COMPARE.md`: что выдумал bare; что rich исправил; что оба пропустили; ваш вердикт.

### C. Два сценария анализа (≈45–60 мин)

`analysis/scenarios/`:

1. Funnel snapshot (шаги, конверсии, окно).  
2. Feedback themes (desk/synthetic ok с меткой).

### D. n8n flow #3 (≈45–75 мин)

```
Schedule (или Manual + план schedule)
  → Read metrics / STATUS / evidence
  → LLM summary
  → Write runs/n8n/digest-metrics-<date>.md
```

[`flow-03-analytics-digest.json`](../sul/n8n/flow-03-analytics-digest.json). На сдаче: 1 Execute + пометка «schedule configured» в README.

### E. S4 protocol design (≈60–90 мин)

1. Скопируйте [`pretest-protocol.md`](../sul/templates/pretest-protocol.md) → `runs/pretest/PROTOCOL-H__.md`.  
2. Заполните: гипотеза, A/B, **N plan 50–100**, seed, artifact URL **своего** продукта, success event = Z, between-subject.  
3. Опционально smoke 3–5 агентов → `runs/pretest/smoke/` (не засчитывается как S4).

### F. Чтение (≈20 мин)

AgentA/B abstract refresh · pretest protocol целиком.

---

## Артефакты сдачи

- `context/*`  
- `analysis/bare.md`, `rich.md`, `COMPARE.md`  
- ≥2 сценария в `analysis/scenarios/`  
- `runs/n8n/digest-metrics-*.md` + flow #3 в README  
- `runs/pretest/PROTOCOL-H__.md`  

---

## Критерии приёмки

[`checklist.md`](./checklist.md).

---

## Оценка часов

| Блок | Часы |
|---|---|
| Context pack | 1–1,5 |
| Bare vs rich | 1–1,5 |
| Сценарии | 0,75–1 |
| n8n #3 | 0,75–1,25 |
| Protocol S4 | 1–1,5 |
| **Итого** | **4–6** |

<!-- week-nav -->
---

**Навигация:** [Н6 индекс](./README.md) · [brief](./student-brief.md) · [checklist](./checklist.md) · [Н7 →](../week-07/)

