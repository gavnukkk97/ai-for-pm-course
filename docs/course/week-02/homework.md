# Н2 · Домашнее задание — ICP, конкуренты, банк персон (S1 старт)

**Срок:** до занятия Н3.  
**Оценка часов:** **4–6 ч**.  
**Связанные файлы:** [`student-brief.md`](./student-brief.md) · [`checklist.md`](./checklist.md) · [`lecture.md`](./lecture.md)  
**SUL веха:** **S1 старт** — [`../sul/personas/persona-bank-guide.md`](../sul/personas/persona-bank-guide.md) · [`../sul/personas/persona.schema.json`](../sul/personas/persona.schema.json)

---

## Зачем

Research pack по **своему** продукту → банк персон (≥10 сейчас, план ≥15 к Н3). Без анти-ICP и sources банк раздуется до «среднего пользователя».

---

## Задачи

### A. Research pack (≈2–2,5 ч)

Создайте `research/`:

| Файл | Минимум |
|---|---|
| `icp.md` | кто / **не кто** / каналы / WTP-proxy / 2–3 job stories |
| `competitors.md` | ≥5 позиций: прямые + **заменитель №1** («ничего»/Notes/Excel…) + JTBD overlap |
| `utp-hypothesis.md` | одна строка УТП + **≥2 falsifiers** |
| `sources.md` | каждый ключевой claim с меткой `live` / `desk` / `assumption` |

### B. Банк персон S1 (≈2–3 ч)

1. Прочитайте [`persona-bank-guide.md`](../sul/personas/persona-bank-guide.md) + schema.  
2. Создайте **≥10** персон `personas/P01.md` … с id `P##`.  
3. **≥3** разных `segment` (разные JTBD/constraints, не разные имена).  
4. Поля схемы заполнены (Markdown-эквивалент ok).  
5. `personas/INDEX.md`: таблица id · segment · JTBD · source class.  
6. В INDEX — обещание довести до **≥15** к Н3.

Антипаттерн: «Мария, 32, любит эффективность» без constraints и sources.

### C. Чтение (≈30–45 мин)

1. Schema + bank guide.  
2. Один YT: [Building synthetic users…](https://www.youtube.com/watch?v=b4MUT_NSq7M) *или* [What are Synthetic Users?](https://www.youtube.com/watch?v=w-bZckedky8).  
3. Skim pm-skills market-research.

---

## Артефакты сдачи

- `research/icp.md`, `competitors.md`, `utp-hypothesis.md`, `sources.md`  
- `personas/P##.md` (≥10) + `personas/INDEX.md`  
- Обновлённый статус S1 в `sul/README.md` (started)

---

## Критерии приёмки

[`checklist.md`](./checklist.md).

---

## Оценка часов

| Блок | Часы |
|---|---|
| ICP + конкуренты + УТП + sources | 2–2,5 |
| ≥10 персон + INDEX | 2–3 |
| Чтение | 0,5 |
| **Итого** | **4–6** |

---

## Связь с n8n

На Н2 новый flow не обязателен; flow #1 должен оставаться зелёным. Signals для digest появятся на Н3.
