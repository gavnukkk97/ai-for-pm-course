# Н5 · Instructor notes — эталон дерева Ритма

## Цель демо (~30–35 мин)

Показать дерево Ритма (activation → retention → paywall conversion) и ритуал **агент считает → человек калибрует**.

---

## Prep

- [ ] Урезанный data dictionary / PRODUCT_CONTEXT Ритма (из product-analytics-ai-course).  
- [ ] Демо-числа на слайде (не прод БД).  
- [ ] Нарочно «галлюцинированный CAC» в ответе агента.

---

## Скрипт A — Дерево (15 мин)

1. NS: Weekly Active Habit Keepers (определить окно).  
2. Драйверы: D1 check-in, D7 retention, paywall view→pay.  
3. Рычаги: онбординг, цена, напоминания.  
4. Связать H01–H03 с узлами.

## Скрипт B — Unit + калибровка (15 мин)

1. Unit = paying user / month.  
2. Агент считает base/upside/downside.  
3. Показать ошибку CAC → человек правит DEFINITIONS.  
4. Фраза: «evals-lite для чисел = калибровочный лог».

## Скрипт C — Мост к S4 (5 мин)

Какая Z из гипотез станет success event претеста — указать на дереве.

---

## Типичные сбои

| Симптом | Реакция |
|---|---|
| Дерево = список KPI без связей | Требовать стрелки/иерархию |
| Сценарии без DEFINITIONS | Блокер |
| Скопированы числа Ритма | Вернуть к своему продукту |
| «У нас нет данных» → пусто | Честные assumptions + plan замера |

---

## Не делать

Повтор полной лекции LTV/CAC с нуля — только шпаргалка и практика калибровки.

---

## Эталоны / playbook

- **Эталон дерево + unit:** [`../instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md`](../instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md)
- Playbook: [`../instructor/playbook-0-8.md`](../instructor/playbook-0-8.md)
