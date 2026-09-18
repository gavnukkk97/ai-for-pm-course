# Evals — backlog-status (lite)

Положить рядом со skill в студенческом репо: `evals/backlog-status.md`.

## Golden 1 — пустой бэклог

**Input:** `backlog/items.md` без пунктов (только заголовок).  
**Expect:** `STATUS.md` явно говорит «пусто»; нет выдуманных id; counts = 0.

## Golden 2 — missing owner

**Input:** один пункт `status=todo`, `owner` пустой.  
**Expect:** пункт в таблице; блок **blockers** содержит этот id; focus не игнорирует блокер.

## Golden 3 — all done

**Input:** ≥3 пункта со `status=done`.  
**Expect:** counts.done = N; suggested focus = нет открытой работы (или только maintenance), без новых выдуманных задач.
