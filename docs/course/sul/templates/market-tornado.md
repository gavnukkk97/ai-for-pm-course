# S3 · Market tornado template

Скопируйте в `strategy/tornado.md` (или Excel с тем же каркасом).  
Веха **S3** · недели **Н4–Н5**.

Цель: bottom-up sizing + чувствительность ≥3 допущений. Не «TAM из статьи».

---

## 1. Сегменты (из банка персон)

| Segment slug | Reach (число) | Source (live/desk/assumption) | Notes |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

## 2. Base case pipeline

Одинаковая логика на сегмент, затем сумма.

```text
Reach → Eligible% → Aware/Trial% → Paid% → ARPU / impact proxy → Result
```

| Шаг | Base | Источник |
|---|---|---|
| Reach total | | |
| Eligible % | | |
| Trial % | | |
| Paid % | | |
| ARPU / value proxy | | |
| **Result** | | |

Краткий вывод base (1–2 предложения):

>

---

## 3. Tornado (± одно допущение за раз)

Меняйте **только одну** переменную относительно base; остальное фиксируйте.

| Допущение | Low | Base | High | Result@Low | Result@High | Δ vs base | Priority |
|---|---|---|---|---|---|---|---|
| Reach | | | | | | | |
| Trial % | | | | | | | |
| Paid % / price | | | | | | | |
| _(своё)_ | | | | | | | |

```mermaid
flowchart LR
  B[Base result] --> T1[± Reach]
  B --> T2[± Trial]
  B --> T3[± Price/Paid]
  T1 --> Rank[Rank by |Δ|]
  T2 --> Rank
  T3 --> Rank
  Rank --> Focus[Живое исследование в топ-1]
```

---

## 4. Decision

| Вопрос | Ответ |
|---|---|
| Топ-1 чувствительность | |
| Что это значит для ставки | go / no-go / thin-bet |
| Чего **не** решили бы по этим числам | |
| Следующий живой шаг | |

---

## 5. Связь с гипотезами

| Допущение tornado | Гипотеза H__ | Как претест проверит |
|---|---|---|
| | | |
