# Н7 · Домашнее задание — питч, ЛПР-спарринг, претест S4

**Срок:** до занятия Н8 (капстоун).  
**Оценка часов:** **4–6 ч** (прогон N≥50 может занять основное время + API cost).  
**Связанные файлы:** [`student-brief.md`](./student-brief.md) · [`checklist.md`](./checklist.md) · [`lecture.md`](./lecture.md)  
**SUL веха:** **S4 run** — [`../sul/templates/pretest-protocol.md`](../sul/templates/pretest-protocol.md) · [`../sul/runners/`](../sul/runners/) · sample REPORT [`../sul/runners/runs/demo-h02-landing-n60/REPORT.md`](../sul/runners/runs/demo-h02-landing-n60/REPORT.md)

---

## Зачем

Упаковать ставку для стейкхолдера и **прогнать** between-subject претест ≥50 агентов на артефакте своего продукта. Smoke с Н6 не засчитывается.

---

## Задачи

### A. Питч-дек (≈60–90 мин)

`pitch/deck.md` (или PDF) — **7±2** секции:

1. Контекст ICP / проблема.  
2. Инсайт (discovery).  
3. Ставка (Н4).  
4. Что симулировали (дизайн S4).  
5. Результат (метрики + 3 темы) — можно черновик до прогона, **обновить** после.  
6. Что *не* доказали.  
7. Ask: живой шаг + ресурсы.

### B. Спарринг с ИИ-ЛПР (≈45–60 мин)

1. `pitch/lp-brief.md` — роль, цели, красные линии.  
2. 10–15 возражений в harness.  
3. `pitch/SPARRING.md` — топ-5 ударов + что изменили в деке.  
4. Запрещено: ЛПР, который всегда соглашается.

### C. Претест S4 (≈2–3,5 ч + API)

1. Финализируйте `runs/pretest/PROTOCOL-H__.md`.  
2. N **≥50** (цель **50–100**); between-subject; seed / модель / temperature зафиксированы.  
3. 2 варианта артефакта **своего** продукта.  
4. Логи: `runs/pretest/<run_id>/` — assignments, raw (без ключей), aggregate.  
5. `REPORT.md`:

| Блок | Обязателен |
|---|---|
| Дизайн | да |
| Таблица метрик A vs B | да |
| Qualitative themes | да |
| Смещения / валидность | да |
| Вердикт supports / rejects / inconclusive | да |
| Следующий живой шаг | да |

Оркестрация: n8n-батч *или* [`pretest_runner.py`](../sul/runners/pretest_runner.py) / ноутбук — главное воспроизводимость.

Дешёвая модель ok при том же seed-протоколе. Предупредите себя о стоимости API.

### D. Чтение (≈30 мин)

AgentA/B · SimAB abstract · pm-skills GTM skim.

---

## Артефакты сдачи

- `pitch/deck.md` (+ обновлён после прогона)  
- `pitch/lp-brief.md`, `pitch/SPARRING.md`  
- `runs/pretest/<run_id>/` + `REPORT.md`  
- Статус S4 в `sul/README.md`

---

## Критерии приёмки

[`checklist.md`](./checklist.md).

---

## Оценка часов

| Блок | Часы |
|---|---|
| Дек + спарринг | 1,5–2,5 |
| Прогон N≥50 + отчёт | 2–3,5 |
| Чтение | 0,5 |
| **Итого** | **4–6** |
