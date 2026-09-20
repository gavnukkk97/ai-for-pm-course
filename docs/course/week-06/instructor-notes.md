# Н6 · Instructor notes — bare vs rich на Ритме

## Цель демо (~40 мин)

Один вопрос про Ритм: bare проваливается → rich даёт действие. Затем намёк на schedule digest и pretest protocol.

---

## Prep

- [ ] CSV-заглушка событий Ритма (или таблица Markdown).  
- [ ] Короткий PRODUCT_CONTEXT + dictionary.  
- [ ] Вопрос: «Почему paywall conversion просел на прошлой неделе?»  
- [ ] n8n schedule workflow draft.  
- [ ] Распечатанный/открытый pretest-protocol template.

---

## Скрипт A — Bare fail (10 мин)

1. Новый чат, без контекста.  
2. Показать выдуманные причины («iOS 18 баг») при отсутствии поля platform.  
3. Класс ловит галлюцинации.

## Скрипт B — Rich (20 мин)

1. Подключить context pack.  
2. Тот же вопрос → ответ с оговорками и join keys.  
3. Человек калибрует: «недели несравнимы — релиз онбординга».  
4. COMPARE.md live в 5 строк.

## Скрипт C — Digest + S4 (10 мин)

1. Показать schedule node.  
2. Открыть protocol: between-subject, N, seed.  
3. Smoke 1 персона × 2 варианта на лендинге Ритма (устно или 1 прогон).  
4. Домашка: pack + protocol на своём продукте.

---

## Типичные сбои

| Симптом | Реакция |
|---|---|
| Rich = просто длинный промпт в чате | Требовать файлы в git |
| Нет COMPARE | Блокер недели |
| Protocol с within-subject | Исправить |
| Schedule без артефакта в runs/ | Один ручной digest минимум |

---

## Ops

Не светить prod credentials Metabase Ритма; только файлы-заглушки.

---

## Эталоны / playbook

- **Эталон bare vs rich:** [`../instructor/rhythm-exemplars/05-bare-vs-rich-context-pack.md`](../instructor/rhythm-exemplars/05-bare-vs-rich-context-pack.md)
- n8n flow #3: [`../sul/n8n/flow-03-description.md`](../sul/n8n/flow-03-description.md) · JSON [`../sul/n8n/flow-03-analytics-digest.json`](../sul/n8n/flow-03-analytics-digest.json)
- S4 runner: [`../sul/runners/README.md`](../sul/runners/README.md)
- Playbook: [`../instructor/playbook-0-8.md`](../instructor/playbook-0-8.md)
