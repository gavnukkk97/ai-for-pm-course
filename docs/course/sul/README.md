# Synthetic User Lab (SUL) — starter kit

Флагман курса «AI для продакта». Вы собираете лабораторию **на своём продукте**; преподаватели параллельно показывают эталон на **Ритме**.

Вехи программы (не урезаем): **S0 → S5**. Этот каталог — каркас **S0** + заготовки под следующие вехи.

| Веха | Неделя | Что здесь уже есть | Что допишете вы |
|---|---|---|---|
| **S0** Scaffold | 1 | контракт папок, skill, n8n flow #1, notice, рубрика-заготовка | README под свой продукт, зелёные контуры |
| **S1** Personas | 2–3 | `persona.schema.json` + пример | ≥15 персон, ≥3 сегмента |
| **S2** Hypotheses | 3–4 | шаблон гипотезы | 5–7 гипотез X→Y→Z |
| **S3** Market eval | 4–5 | — | sizing + tornado |
| **S4** Prefest | 6–7 | — | ≥50–100 агентов, 2 варианта |
| **S5** Defense | 8 | [`validity-rubric-stub.md`](./validity-rubric-stub.md) | честная защита |

Теоретический фундамент: AgentA/B (arXiv 2504.09723), урок 4.6 `stats-ab-course`, ethics notice как в voice-of-agents.

---

## Быстрый старт S0

```bash
# из вашего репо курса / рабочего кейса
cp -R path/to/docs/course/sul ./sul-lab
cd sul-lab
# отредактируйте README (этот файл), product link, notice
```

1. Прочитайте [`folder-contract.md`](./folder-contract.md).  
2. Подключите skill [`skills/backlog-status/`](./skills/backlog-status/) к Cursor или Claude Code.  
3. Импортируйте n8n [`n8n/flow-01-webhook-to-artifact.json`](./n8n/flow-01-webhook-to-artifact.json) — см. [`n8n/flow-01-description.md`](./n8n/flow-01-description.md).  
4. Заполните блок «Мой продукт» ниже.  
5. Отметьте чеклист S0 в [`../week-01/checklist.md`](../week-01/checklist.md).

---

## Мой продукт (заполните)

| Поле | Значение |
|---|---|
| Название | _…_ |
| URL / артефакт для претеста | _…_ |
| Сегменты (черновик) | _…_ |
| Harness | Cursor / Claude Code |
| n8n | local :5678 / cloud URL |
| Имя workflow #1 | _…_ |
| Как запускать flow #1 | Manual / Webhook … |

---

## Дерево

```text
sul/
├── README.md                 ← вы здесь
├── folder-contract.md
├── SYNTHETIC-DATA-NOTICE.md
├── validity-rubric-stub.md   ← дорастёт к S5
├── personas/
│   ├── persona.schema.json
│   └── examples/persona-example.md
├── hypotheses/
│   └── _TEMPLATE.md
├── runs/
│   └── .gitkeep              ← сюда логи прогонов (S2+)
├── skills/
│   └── backlog-status/SKILL.md
├── n8n/
│   ├── flow-01-description.md
│   └── flow-01-webhook-to-artifact.json
└── templates/
    └── decision-memo-stub.md
```

---

## Границы (повторять в каждом отчёте)

- Синтетический пользователь **смещён**.  
- Совпадение направления с живым тестом **не доказано** для вашего домена, пока не сделаете калибровку (S5).  
- Для: отбраковки гипотез, подготовки интервью, чувствительности.  
- Не для: финального ship/kill без живых данных, если трафик позволяет.

---

## Связанные материалы курса

- Программа §3: [`../../program.md`](../../program.md)  
- Неделя 1: [`../week-01/`](../week-01/)  
- Источники: [`../../external-materials.md`](../../external-materials.md)
