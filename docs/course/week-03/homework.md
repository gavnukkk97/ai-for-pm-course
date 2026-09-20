# Н3 · Домашнее задание — Discovery, гипотезы S2, n8n digest #2

**Срок:** до занятия Н4.  
**Оценка часов:** **4–6 ч**.  
**Связанные файлы:** [`student-brief.md`](./student-brief.md) · [`checklist.md`](./checklist.md) · [`lecture.md`](./lecture.md)  
**SUL вехи:** **S1 gate** (≥15 персон) · **S2 старт** — [`../sul/hypotheses/_TEMPLATE.md`](../sul/hypotheses/_TEMPLATE.md) · [`../sul/hypotheses/hypothesis-runner-stub.md`](../sul/hypotheses/hypothesis-runner-stub.md) · n8n [`../sul/n8n/flow-02-description.md`](../sul/n8n/flow-02-description.md)

---

## Зачем

Дожать персон → сформулировать 5–7 гипотез X→Y→Z → упаковать discovery (Минто) → первый signals→digest в n8n.

---

## Задачи

### A. S1 gate (≈45–60 мин)

1. Доведите банк до **≥15** персон, **≥3** сегмента.  
2. Обновите `personas/INDEX.md`.  
3. В `sul/README.md` статус S1 = done (или almost + что осталось ≤2 персоны — только с разрешением instructor).

### B. Гипотезы S2 (≈2–2,5 ч)

1. Создайте **5–7** файлов `hypotheses/H01.md` … по [`_TEMPLATE.md`](../sul/hypotheses/_TEMPLATE.md).  
2. У каждой обязательно:
   - **X→Y→Z** (Z = измеримый success event, не «улучшим UX»);
   - `variants` (A/B или оффер/нет);
   - `artifact` своего продукта;
   - **≥2** red-team пункта.
3. ≥1 заполненный runner-plan: `hypotheses/runners/H0X-plan.md` по [`hypothesis-runner-stub.md`](../sul/hypotheses/hypothesis-runner-stub.md) (метрика без дыр, between-subject).

### C. Evidence + brief (≈60–90 мин)

1. `evidence/` — заметки/ссылки с метками источников (≥5 записей или файлов).  
2. `evidence/REDTEAM.md` — сводный red-team (или ссылки внутрь H__).  
3. `discovery/BRIEF.md` (≤1 стр., Минто):
   - ответ сверху (главная проблема ICP);
   - 3 аргумента;
   - H01–H0N одной строкой;
   - что *не* узнаем без живых людей.

### D. n8n flow #2 (≈60–90 мин)

```
Schedule или Manual
  → Read evidence/inbox/*.md (или Webhook JSON)
  → LLM: сводка сигналов; top-5; дыры
  → Write runs/n8n/digest-<date>.md
```

Import: [`flow-02-signals-to-digest.json`](../sul/n8n/flow-02-signals-to-digest.json).  
В `sul/README.md` — имя workflow #2 и запуск. Credentials только в UI.

### E. Чтение (≈30 мин)

[voice-of-agents](https://github.com/blakeaber/voice-of-agents) README · AgentA/B between-subject (5 строк конспекта в `notes/agentab-between.md`).

---

## Артефакты сдачи

- ≥15 персон + INDEX  
- 5–7 гипотез + ≥1 runner-plan  
- `discovery/BRIEF.md` + evidence/REDTEAM  
- `runs/n8n/digest-*.md` + запись flow #2 в README  

---

## Критерии приёмки

[`checklist.md`](./checklist.md).

---

## Оценка часов

| Блок | Часы |
|---|---|
| S1 gate | 0,75–1 |
| Гипотезы + runner | 2–2,5 |
| Brief + evidence | 1–1,5 |
| n8n #2 | 1–1,5 |
| **Итого** | **4–6** |

<!-- week-nav -->
---

**Навигация:** [Н3 индекс](./README.md) · [brief](./student-brief.md) · [checklist](./checklist.md) · [Н4 →](../week-04/)

