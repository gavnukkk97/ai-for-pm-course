# Н1 · Домашнее задание — экзоскелет, n8n #1, SUL S0

**Срок:** до занятия Н2.  
**Оценка часов:** **4–6 ч**.  
**Связанные файлы:** [`student-brief.md`](./student-brief.md) · [`checklist.md`](./checklist.md) · [`lecture.md`](./lecture.md)  
**SUL веха:** **S0** — [`../sul/`](../sul/) · [`../sul/folder-contract.md`](../sul/folder-contract.md) · [`../sul/n8n/flow-01-description.md`](../sul/n8n/flow-01-description.md)

---

## Зачем

Собрать четыре зелёных контура: **harness · skill+evals · n8n #1 · SUL scaffold** на своём продукте.

---

## Задачи

### A. Контракт harness (≈60–90 мин)

1. Скопируйте каркас из [`../sul/`](../sul/) в **свой** репозиторий.  
2. Правила в `.cursor/rules/` *или* `AGENTS.md` *или* `CLAUDE.md`:
   - читать `product/ONEPAGER.md` перед генерацией;
   - не выдумывать метрики без определения;
   - метки `live` / `synthetic` / `assumption`.
3. Skill `backlog-status` (текст из [`../sul/skills/backlog-status/`](../sul/skills/backlog-status/)).  
4. `backlog/items.md` — 5–10 пунктов → вызов skill → `backlog/STATUS.md` на диске.  
5. `evals/backlog-status.md` — **≥3** golden cases.

### B. n8n flow #1 (≈90–120 мин)

Цепочка: **триггер → LLM (или mock) → Markdown-артефакт**.

1. Import [`../sul/n8n/flow-01-webhook-to-artifact.json`](../sul/n8n/flow-01-webhook-to-artifact.json) *или* соберите по [`flow-01-description.md`](../sul/n8n/flow-01-description.md).  
2. Один успешный Execute; output ≠ lorem (сводка по вашему бэклогу/1-pager).  
3. Сохраните артефакт в `runs/n8n/flow01-last.md` (Cloud: копипаст из execution ok).  
4. В `sul/README.md`: URL инстанса, имя workflow, как запускать.  
5. Export JSON **без** API keys.

### C. SUL S0 (≈60–90 мин)

1. Папки по [`folder-contract.md`](../sul/folder-contract.md): `personas/`, `hypotheses/`, `runs/`, `skills/`.  
2. `SYNTHETIC-DATA-NOTICE.md` на месте.  
3. Блок «Мой продукт» в `sul/README.md` заполнен.  
4. Dry-run harness: агент видит контракт папок (короткий лог в `runs/s0-dry-run.md`).

---

## Артефакты сдачи

| Путь | Контур |
|---|---|
| Rules / CLAUDE / AGENTS | harness |
| skill `backlog-status` + `backlog/STATUS.md` + `evals/…` | skill |
| n8n workflow + `runs/n8n/flow01-last.md` + запись в README | n8n #1 |
| `sul/README.md` + notice + папки | S0 |

Сдача: ссылка на репо (или zip).

---

## Критерии приёмки

[`checklist.md`](./checklist.md). Коротко — четыре зелёных контура без секретов в git.

---

## Оценка часов

| Блок | Часы |
|---|---|
| Копирование SUL + rules | 0,5–1 |
| Skill + evals + прогон | 1–1,5 |
| n8n #1 | 1,5–2 |
| S0 README + dry-run | 1–1,5 |
| **Итого** | **4–6** |

---

## Чтение

Cursor Skills / Claude Code custom skills · [n8n AI intro](https://docs.n8n.io/advanced-ai/intro-tutorial/) · AgentA/B abstract (границы).
