# Н1 · Checklist приёмки

## Harness

- [ ] Rules / `CLAUDE.md` / `AGENTS.md` читают `product/ONEPAGER.md` и запрещают выдуманные метрики.  
- [ ] Skill `backlog-status` в репо; вызов обновляет `backlog/STATUS.md` на диске.  
- [ ] `evals/backlog-status.md` — ≥3 golden cases.  
- [ ] Студент может объяснить: skill vs разовый промпт.

## n8n flow #1

- [ ] Workflow существует; есть ≥1 успешный execution.  
- [ ] Цепочка: триггер → LLM (или документированный mock) → артефакт.  
- [ ] Описание запуска в `sul/README.md`.  
- [ ] Export без секретов (или секреты только в UI credentials).

## SUL S0

- [ ] Папки: `personas/`, `hypotheses/`, `runs/`, `skills/` (или эквивалент по [`folder-contract`](../sul/folder-contract.md)).  
- [ ] README SUL заполнен под **свой** продукт.  
- [ ] `SYNTHETIC-DATA-NOTICE.md` на месте.  
- [ ] Dry-run harness по контракту папок прошёл.

## Красные флаги

- S0 только скринами чата, без файлов в git.  
- Ключи API в Markdown/JSON.  
- «Персоны» уже сгенерированы как «средний пользователь» без сегментов (рано для S1, но если есть — вернуть).  
- n8n-сценарий = автопостинг в соцсети (вне скоупа).
