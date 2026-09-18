# Н1 · Lesson outline — AI-экзоскелет + n8n + S0

| Поле | Значение |
|---|---|
| **Неделя** | 1 · живое занятие ~1,5 ч + практика 4–6 ч |
| **Артефакты** | Harness fluency · 1 skill · 1 n8n flow · **SUL S0** |
| **Демо instructor** | Тот же flow на файлах Ритма |

---

## Цели

После Н1 студент:

1. Свободно ведёт процесс в **≥1 harness**: правила репо + skill + evals-lite (чеклист приёмки агента).  
2. Собран агент **«бэклог → статус»** (skill читает файлы бэклога, пишет статус-таблицу).  
3. Собран **n8n flow #1**: триггер (webhook *или* Manual) → LLM-шаг → артефакт (файл Markdown / строка в таблице).  
4. Поднят **SUL S0**: структура папок + README + dry-run harness + n8n flow привязан к репо.

---

## Теория коротко (слайды / 40–50 мин)

### 1. Harness = продукт процесса

Не «чат с моделью», а контур: **контекст (файлы) → навыки (skills) → guardrails (rules) → evals (человек + golden cases)**.

Язык занятия: Medium «Why PM care about Agent Harness» (пересказ, не копипаст) + офиц. docs Cursor Skills / Claude Code skills.

| Примитив | Cursor | Claude Code |
|---|---|---|
| Постоянный контекст | Rules / `AGENTS.md` | `CLAUDE.md` |
| Процедура по запросу | Skill (`SKILL.md`) | Skill (`.claude/skills/…`) |
| Внешние инструменты | MCP | MCP |
| Приёмка | чеклист + golden files | то же |

### 2. Skill vs промпт

Промпт — разовый. Skill — версионируемая процедура в git: когда вызывать, какие входы/выходы, что запрещено.

Эталон библиотек (ставить выборочно, не «все 68»): [phuryn/pm-skills](https://github.com/phuryn/pm-skills), опционально [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills).

### 3. Evals-lite (минимум курса)

До LLM-as-judge:

1. ≥3 **golden cases** (вход → ожидаемые поля выхода).  
2. Чеклист человека (метрика определена? источники? нет «среднего пользователя»?).  
3. Seed / температура зафиксированы, где есть генерация.

### 4. n8n в ядре (не SMM)

Сценарий Н1: **триггер → LLM → файл/таблица**. Зачем: воспроизводимый запуск, webhook из форм/CI, позже — digests и прогоны SUL.

Опора: [n8n AI intro tutorial](https://docs.n8n.io/advanced-ai/intro-tutorial/) · [Webhook node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) · [Read/Write Files](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/).

### 5. SUL S0 — контракт папок

`personas/` · `hypotheses/` · `runs/` · `skills/` + README + `SYNTHETIC-DATA-NOTICE`.  
Подробно: [`../sul/`](../sul/).

### 6. Границы (обязательный слайд)

Синтетический пользователь смещён. Для отбраковки и подготовки интервью — да. Для финального ship/kill без живых данных — нет (если трафик позволяет). Опора: AgentA/B, урок 4.6 stats-ab.

---

## Практика (ядро)

См. [`student-brief.md`](./student-brief.md).

1. Rules/`CLAUDE.md` под свой продукт.  
2. Skill `backlog-status` (шаблон в SUL).  
3. n8n flow #1 по описанию + import JSON.  
4. Инициализация SUL S0 в своём репо.

---

## Тайминг живого занятия (пример)

| Мин | Блок |
|---|---|
| 0–10 | Разбор 1-pager (2–3 примера) |
| 10–35 | Harness: skill live на Ритме |
| 35–55 | n8n flow #1 live на Ритме |
| 55–70 | S0 контракт + этика синтетики |
| 70–90 | Q&A / разбор блокеров Docker |

---

## Materials

[`../materials-by-module.md`](../materials-by-module.md) §Н1 · [`../../external-materials.md`](../../external-materials.md).
