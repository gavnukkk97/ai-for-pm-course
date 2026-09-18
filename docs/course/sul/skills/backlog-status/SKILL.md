---
name: backlog-status
description: Use when the user asks to refresh backlog status, triage blockers, or turn backlog/items.md into backlog/STATUS.md. Reads backlog files and writes a status table plus risks.
---

# backlog-status

## When to use

- Нужна актуальная таблица статусов бэклога из файлов репо.  
- Перед синкамом / сдачей недели.  
- После того, как человек правил `backlog/items.md`.

## Inputs

- Читать: `backlog/items.md` (или `backlog/*.md`, если items разбиты).  
- Читать контекст продукта: `product/ONEPAGER.md`, если есть.  
- Не выдумывать пункты, которых нет в файлах.

## Output

Записать (создать/перезаписать) `backlog/STATUS.md`:

1. Дата/время обновления (ISO).  
2. Таблица: `id | title | status | owner | next | blockers`.  
3. Блок **Counts** по статусам.  
4. Блок **Risks / blockers** — только из данных файлов; если owner пустой и status ≠ done → блокер.  
5. Блок **Suggested focus (top 3)** — с пометкой `assumption`, если приоритет не задан в файле.

## Rules

- Язык: русский (id/status можно EN).  
- Если бэклог пуст — STATUS с явной фразой «пусто», не генерировать фейковые задачи.  
- Не менять `backlog/items.md`, пока пользователь не просит.  
- В конце ответа человеку: список изменённых путей.

## Evals (golden)

Сверяй с `evals/backlog-status.md`, если файл есть. Минимум:

1. Пустой backlog → STATUS без выдуманных id.  
2. Пункт без owner → в blockers.  
3. Все done → focus = «нет открытых», не придумывать работу.
