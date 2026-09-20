# Плейсхолдер · n8n список Workflows

> **«плейсхолдер → заменить скрином»**  
> Целевой файл: [`../n0-n8n-workflows-empty.png`](../n0-n8n-workflows-empty.png) (ещё нет — пишет kir с local `:5678` **или** Cloud).  
> Идея скрина: UI «Workflows» с **одним** сохранённым пустым flow. Без секретов, без LLM-нод на Н0.

На Н0 достаточно «инстанс жив + workflow сохранён» — не рабочий AI-flow.

```mermaid
flowchart LR
  subgraph n8nUI["n8n UI · local :5678 или Cloud"]
    direction TB
    Nav["Меню: Workflows"]
    List["Список workflows"]
    One["My empty workflow<br/>Active: off · nodes: 0–1"]
    Nav --> List --> One
  end
  Open["Open / New workflow"] --> Save["Save ★"]
  Save --> One
```

```text
n8n ──────────────────────────────────
│ Overview │ Workflows │ Credentials │
│            ▲ вы здесь               │
├─────────────────────────────────────┤
│ Name                 │ Updated      │
│ My empty workflow    │ сегодня      │  ← один сохранённый
│ (можно без нод)      │              │
└─────────────────────────────────────┘
```

**Сдача Н0:** скрин этого списка *или* export JSON пустого flow → `runs/n8n/n0-empty-workflow.json`.
