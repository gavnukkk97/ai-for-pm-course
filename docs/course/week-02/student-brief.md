# Н2 · Student brief — ICP, конкуренты, банк персон

Практика **4–6 ч**. Сдача: папка `research/` + `personas/` (≥10 файлов) в вашем SUL-репо.

Всё — про **свой** продукт из 1-pager Н0. Ритм только как образец структуры на занятии.

---

## A. Research pack

Создайте `research/`:

| Файл | Содержание (минимум) |
|---|---|
| `icp.md` | Кто ICP / анти-ICP / платёжный контекст / 2–3 канала / 1 абзац «почему сейчас» |
| `competitors.md` | ≥5 строк: имя · тип (прямой/косвенный/заменитель) · JTBD overlap · чем слабее/сильнее для *вашего* ICP |
| `utp-hypothesis.md` | 1–2 предложения УТП + 3 falsifiers («опровергнется, если…») |
| `sources.md` | Ссылки/скрины/заметки; каждая помечена `live` / `desk` / `assumption` |

**Запрещено:** ICP = «все пользователи смартфонов»; конкуренты только из рекламы без JTBD.

---

## B. Банк персон (S1 старт)

1. Прочитайте [`../sul/personas/persona-bank-guide.md`](../sul/personas/persona-bank-guide.md) и схему.  
2. Заведите ≥**3** именованных сегмента (slug в `segment`).  
3. Создайте ≥**10** персон (`P01`…): Markdown *и/или* JSON по схеме.  
4. У ≥ половины `source` ∈ {`interview`, `analytics_cluster`, `desk_research`, `mixed`} — не чистый `llm_draft`.  
5. У каждой: JTBD ≥1 абзац, ≥1 constraint, ≥1 channel, `bias_notes`.  
6. В `personas/INDEX.md` — таблица id · segment · source · статус.

К Н3 доведите до **≥15** (критерий S1).

---

## C. Harness + n8n (лёгкий дожим)

- Skill или разовое задание агенту: «проверь все персоны на антипаттерн среднего пользователя; список дыр в `personas/QA.md`».  
- Опционально: n8n Manual → LLM → сводка `research/digest-week02.md` из `icp.md` + `competitors.md`.

---

## D. Чтение (минимум)

1. Schema + example в `sul/personas/`.  
2. [Building synthetic users…](https://www.youtube.com/watch?v=b4MUT_NSq7M) *или* [What are Synthetic Users?](https://www.youtube.com/watch?v=w-bZckedky8) — 1 на выбор.  
3. pm-skills market-research (README plugin) — skim.

---

## Критерии приёмки

[`checklist.md`](./checklist.md).
