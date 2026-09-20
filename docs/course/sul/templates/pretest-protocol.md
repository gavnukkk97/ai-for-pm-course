# S4 · Pretest protocol (≥50–100 агентов)

Скопируйте в `runs/pretest/PROTOCOL-H__.md`.  
Веха **S4** · дизайн на **Н6**, полный прогон на **Н7**.

Опора: AgentA/B (arXiv 2504.09723), SimAB, stats-ab 4.6 — **претест и приоритизация**, не замена живому АБ.

---

## 0. Границы (вставить в каждый REPORT)

- Синтетический пользователь смещён.  
- Совпадение знака с живым тестом не доказано a priori.  
- Вердикт: supports / rejects / **inconclusive** — без стыда.

---

## 1. Гипотеза и артефакты

| Поле | Значение |
|---|---|
| H id | |
| X→Y→Z (кратко) | |
| Primary metric | |
| Guardrail | |
| Artifact A | URL/path |
| Artifact B | URL/path |
| Чем A≠B для пользователя | одна фраза |

---

## 2. Дизайн

| Параметр | Требование курса | Факт |
|---|---|---|
| Design | between-subject | |
| N total | 50–100 | |
| Allocation | ~1:1 | |
| Persona source | банк S1 | |
| Stratification | опц. по segment | |
| Seed | обязателен | |
| Model / temp | зафиксировать | |
| Blind to alternate variant | да | |

**Запрещено:** один агент оценивает A и B подряд; «выбери лучший».

---

## 3. Процедура агента

1. Загрузить персону.  
2. Показать **только** назначенный вариант.  
3. Задача: реалистичное поведение до success / отказ / лимит шагов.  
4. Записать outcome + 1–3 short themes (голос персоны).  
5. Не обновлять память персоны между прогонами.

---

## 4. Логи (минимум)

```text
runs/pretest/<run_id>/
  PROTOCOL.md          ← копия этого файла
  ASSIGNMENTS.csv      ← persona_id,variant,seed_offset
  raw/<persona>_<var>.md
  aggregate.csv        ← outcomes
  REPORT.md
```

`ASSIGNMENTS.csv` колонки: `persona_id,segment,variant,seed,model,outcome,success,themes,path_raw`

---

## 5. Анализ

1. Таблица primary metric A vs B (counts + rate).  
2. Разбивка по segment (если N позволяет; иначе честно «мало»).  
3. Themes: топ-5 на вариант.  
4. Не обязателен p-value; если считаете — оговорить, что это **не** живой АБ.  
5. Sensitivity: exclude llm_draft-only personas — знак держится?

---

## 6. REPORT — обязательные секции

1. Дизайн и N  
2. Метрики  
3. Themes  
4. Validity / смещения  
5. Вердикт + цена ошибки  
6. Следующий живой шаг  

---

## 7. Gate перед запуском полного N

- [ ] Runner stub ready  
- [ ] Smoke N=3–5 без утечки варианта  
- [ ] Бюджет API оценён  
- [ ] Человек утвердил primary metric  
- [ ] Артефакты A/B доступны агенту так же, как будут людям (URL/текст)
