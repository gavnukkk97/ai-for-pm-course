# Н1 · Student brief — экзоскелет, n8n, S0

Практика **4–6 ч**. Сдача: ссылка на репо (или zip) с четырьмя зелёными контурами.

Стартовый каркас копируйте из [`../sul/`](../sul/) в **свой** git-репозиторий (название на ваш вкус). Публичный GitHub курса пока не обязателен.

---

## A. Контракт harness

### Cursor

1. В корне репо: `.cursor/rules/product.mdc` *или* `AGENTS.md` с правилами:
   - язык артефактов: RU (skills/термины EN as-is);
   - всегда читать `product/ONEPAGER.md` перед генерацией;
   - не выдумывать метрики без определения;
   - любой вывод про пользователей помечать: `live` / `synthetic` / `assumption`.
2. Создайте skill `.cursor/skills/backlog-status/SKILL.md` — можно взять из [`../sul/skills/backlog-status/SKILL.md`](../sul/skills/backlog-status/SKILL.md).

### Claude Code

1. `CLAUDE.md` в корне с теми же правилами.  
2. Skill: `.claude/skills/backlog-status/SKILL.md` (тот же текст).

### Задание агенту «бэклог → статус»

1. Положите 5–10 пунктов в `backlog/items.md` (формат: id, title, status, owner, next).  
2. Вызовите skill: обновить `backlog/STATUS.md` таблицей и блоком «риски / блокеры».  
3. **Evals-lite:** в `evals/backlog-status.md` опишите 3 golden cases (например: пустой бэклог; все Done; пункт без owner → должен пометить блокер).

---

## B. n8n flow #1

Цель: **триггер → LLM → Markdown-артефакт**.

Рекомендуемая схема (без секретов в git):

```
Manual Trigger  (или Webhook POST JSON)
    → Set          (нормализовать input: product_name, backlog_snippet, ask)
    → Basic LLM / AI Agent   (credential в UI n8n, не в JSON)
    → Write Binary / Convert to File  →  сохранить summary.md
       или просто → Set + скачать из execution
```

Подробное описание узлов и import: [`../sul/n8n/flow-01-description.md`](../sul/n8n/flow-01-description.md) · JSON: [`../sul/n8n/flow-01-webhook-to-artifact.json`](../sul/n8n/flow-01-webhook-to-artifact.json).

**Минимум приёмки flow #1:**

- [ ] Workflow сохранён и успешно Execute один раз.  
- [ ] На выходе есть текст-сводка по вашему бэклогу/1-pager (не lorem).  
- [ ] В `sul/README.md` указаны: URL инстанса (local/cloud), имя workflow, как запускать.  
- [ ] В экспорте JSON **нет** API keys (credentials = placeholders).

Альтернатива без Write-to-disk (n8n Cloud): узел **Respond to Webhook** или копирование output в `runs/n8n/flow01-last.md` руками после Execute — допустимо на S0, если задокументировано.

---

## C. SUL S0 scaffold

1. Скопируйте дерево из [`../sul/`](../sul/) (кроме чужих секретов).  
2. Заполните `sul/README.md` под **свой** продукт.  
3. Положите `SYNTHETIC-DATA-NOTICE.md` (шаблон в SUL).  
4. Dry-run harness: «прочитай folder-contract и создай пустой `hypotheses/_TEMPLATE.md` по схеме» — файл на месте.  
5. Связка: в README одна фраза, как n8n flow #1 будет позже триггерить прогоны (даже если пока Manual).

Критерий S0 из программы: **README + оба контура (harness dry-run + n8n) зелёные**.

---

## D. Чтение (обязательный минимум)

1. Cursor [Skills](https://cursor.com/docs/skills) *или* Claude Code [custom skills](https://code.claude.com/docs/en/custom-skills) — по вашему harness.  
2. [MCP intro](https://modelcontextprotocol.io/docs/getting-started/intro) — 15 мин, без обязательной установки MCP на этой неделе.  
3. AgentA/B abstract + границы: https://arxiv.org/abs/2504.09723 (и `sul/SYNTHETIC-DATA-NOTICE.md`).  
4. Опционально видео: [Claude for PMs](https://www.youtube.com/watch?v=bITUsUsrxjM) (можно на 1.5×, фокус на skills/MCP).

Полный список: [`../materials-by-module.md`](../materials-by-module.md).

---

## Критерии приёмки

См. [`checklist.md`](./checklist.md).
