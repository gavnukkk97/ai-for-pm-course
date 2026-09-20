# Н3 · Instructor notes — discovery brief на Ритме

## Цель демо (~35 мин)

Эталон: 3 гипотезы paywall/onboarding Ритма в X→Y→Z + red-team + намёк на digest.

---

## Prep

- [ ] ICP Ритма с Н2 под рукой.  
- [ ] Три гипотезы заранее:  
  - H01: paywall на D1 → ↓ activation, ↑ WTP у remaining  
  - H02: social proof на лендинге → ↑ trial start  
  - H03: укороченный онбординг → ↑ D1 check-in  
- [ ] Нарочно «дырявая» Z без знаменателя — для разбора.  
- [ ] n8n: простой Manual → LLM → текст (можно тот же инстанс, новый workflow).

---

## Скрипт A — X→Y→Z (15 мин)

1. Взять H01, разобрать метрику вслух (числитель/окно).  
2. Показать дырявую версию → класс чинит.  
3. Заполнить шаблон гипотезы в репо демо.  
4. Фраза: «нет Z до прогона = нельзя принимать S2».

## Скрипт B — Red-team (10 мин)

1. Атака 1: LLM любит paywall-нарратив → ложный supports.  
2. Атака 2: артефакт = скрин, живые видят другое.  
3. Студенты в парах: 5 мин, 2 атаки на свою H.

## Скрипт C — Brief + n8n (10 мин)

1. Минто: один слайд/файл BRIEF.md на Ритм.  
2. Прогон digest по 3 файлам evidence.  
3. Домашка: 5–7 гипотез + S1≥15.

---

## Типичные сбои

| Симптом | Реакция |
|---|---|
| «Увеличим engagement» без определения | Вернуть к Z-контракту |
| Within-subject «агент видит оба варианта» | Запретить; only between-subject |
| 5 гипотез без artifact URL | Блокер сдачи |
| Digest = рерайт ICP | Требовать новые сигналы из inbox |

---

## Не показывать

Ключи API; private Mail/Ya; полные данные Postgres Ритма — только файлы-заглушки.

---

## Эталоны / playbook

- **Эталон discovery brief:** [`../instructor/rhythm-exemplars/02-discovery-brief.md`](../instructor/rhythm-exemplars/02-discovery-brief.md)
- n8n flow #2: [`../sul/n8n/flow-02-description.md`](../sul/n8n/flow-02-description.md) · JSON [`../sul/n8n/flow-02-signals-to-digest.json`](../sul/n8n/flow-02-signals-to-digest.json)
- Playbook: [`../instructor/playbook-0-8.md`](../instructor/playbook-0-8.md)
