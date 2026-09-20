# Плейсхолдер · n8n canvas flow #1

> **«плейсхолдер → заменить скрином»**  
> Целевой файл: [`../n1-n8n-flow01-canvas.png`](../n1-n8n-flow01-canvas.png) (ещё нет — пишет kir с canvas без секретов в нодах).  
> Идея скрина: цепочка **триггер → normalize → LLM → wrap → артефакт** на холсте n8n.

Подробности узлов: [`../../sul/n8n/flow-01-description.md`](../../sul/n8n/flow-01-description.md).

```mermaid
flowchart LR
  subgraph canvas["n8n · Editor canvas · flow #1"]
    T["1 Manual Trigger<br/>или Webhook"]
    S["2 Set<br/>normalize"]
    L["3 Basic LLM / AI Agent<br/>credential только в UI"]
    W["4 Set<br/>wrap markdown"]
    O["5 Output / Write File<br/>или Respond"]
    T --> S --> L --> W --> O
  end
```

```text
[Manual Trigger]──►[Set normalize]──►[Basic LLM]──►[Set wrap]──►[Output]
       ▲                                    │
   Execute / POST                           credential в UI
   {product_name, backlog_snippet, ask}     (не в git JSON)
```

**Приёмка:** один успешный Execute → осмысленный Markdown-сводка (не lorem); в экспорте нет API keys.
