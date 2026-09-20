# Н4 · Домашнее задание — ставки, sizing, tornado (S3)

**Срок:** до занятия Н5.  
**Оценка часов:** **4–6 ч**.  
**Связанные файлы:** [`student-brief.md`](./student-brief.md) · [`checklist.md`](./checklist.md) · [`lecture.md`](./lecture.md)  
**SUL веха:** **S3** — [`../sul/templates/market-tornado.md`](../sul/templates/market-tornado.md) · [`../sul/templates/decision-memo-stub.md`](../sul/templates/decision-memo-stub.md)

---

## Зачем

Три осмысленные AI-ставки на своём продукте + bottom-up sizing + tornado чувствительности. Синтетика помогает **приоритизировать**, не «утвердить TAM».

---

## Задачи

### A. Три ставки (≈45–60 мин)

`strategy/bets.md` — ровно **3** строки/карточки:

| Поле | Требование |
|---|---|
| Название | глагол + объект |
| Связь с H__ | id гипотез Н3 |
| Цена ошибки | что потеряем, если ставка ложна |
| Kill-критерий | когда сворачиваем |
| Контур | harness / n8n / SUL / человек-приёмка |

Антипаттерн: «используем GPT для всего».

### B. Strategy memo (≈90–120 мин)

`strategy/MEMO.md` (1–2 стр.):

1. Контекст ICP (ссылка на research).  
2. **go / no-go / thin-bet** по каждой ставке.  
3. Bottom-up: сегмент → reach → conv proxy → impact.  
4. Tornado: топ-3 чувствительных допущения.  
5. Абзац: что решили бы / чего **не** решили бы по синтетике.  
6. Следующий живой шаг.

### C. S3 Market eval (≈90–120 мин)

1. Скопируйте [`market-tornado.md`](../sul/templates/market-tornado.md) → `strategy/tornado.md`, заполните.  
2. ≥3 сегмента из банка персон; размер с источником + меткой.  
3. Conv/WTP-proxy: откуда (опрос / аналог / LLM) — пометить.  
4. База + tornado (±% по ≥3 допущениям).  
5. Decision memo для главной ставки: [`decision-memo-stub.md`](../sul/templates/decision-memo-stub.md) → `strategy/decision-memo.md`.

### D. n8n (опционально, ≈30–45 мин)

Manual/Webhook: JSON допущений → LLM QA полноты tornado → `runs/n8n/tornado-qa.md`.

### E. Чтение (≈30 мин)

Abstract [SSR](https://arxiv.org/abs/2510.08338) · README [synthetic-market-research](https://github.com/BayramAnnakov/synthetic-market-research).

---

## Артефакты сдачи

- `strategy/bets.md`  
- `strategy/MEMO.md`  
- `strategy/tornado.md`  
- `strategy/decision-memo.md`  
- Статус S3 в `sul/README.md`

---

## Критерии приёмки

[`checklist.md`](./checklist.md).

---

## Оценка часов

| Блок | Часы |
|---|---|
| Ставки | 0,75–1 |
| Memo + bottom-up | 1,5–2 |
| Tornado + decision | 1,5–2 |
| Чтение / n8n QA | 0,5–1 |
| **Итого** | **4–6** |
