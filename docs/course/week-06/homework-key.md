# Н6 · Ключ / рубрика преподавателя

**Студенту не выдавать целиком.** Выдача: [`homework.md`](./homework.md).  
**Эталон структуры:** [`../instructor/rhythm-exemplars/05-bare-vs-rich-context-pack.md`](../instructor/rhythm-exemplars/05-bare-vs-rich-context-pack.md).  
**n8n:** [`../sul/n8n/flow-03-description.md`](../sul/n8n/flow-03-description.md).  
**Playbook:** [`../instructor/playbook-0-8.md`](../instructor/playbook-0-8.md) §Н6.

---

## Что выглядит хорошо

| Артефакт | Структура | Quality bar |
|---|---|---|
| Context | 4 файла | pitfalls ≥5 конкретны («путает D1 и D7»), не общие |
| Bare/rich | один вопрос | COMPARE честный: rich тоже может ошибаться |
| Funnel/themes | 2 сценария | Окна и дедуп согласованы с DEFINITIONS |
| Flow #3 | digest в git | Schedule задокументирован; без секретов |
| Protocol | pretest template | between-subject; Z=success; N 50–100; свой artifact |

**Отлично:** smoke-лог 3–5 + protocol готов к батчу.  
**Достаточно:** design protocol полный; schedule = Manual с cron-планом.  
**Недостаточно:** rich = «длинный промпт» без файлов в `context/`.

---

## Частые провалы

| Симптом | Ремедиация |
|---|---|
| Bare и rich на разных вопросах | Пересдать COMPARE на одном вопросе |
| Within-subject в protocol | Вернуть AgentA/B; правка protocol |
| Protocol без success event | Привязать к Z из H__ |
| Context только в голове | Файлы в git |
| Schedule без артефакта | Требовать digest-*.md |
| Smoke выдан за S4 | Явно: полный N на Н7 |

---

## Чеклист оценки

- [ ] context pack (4 файла)  
- [ ] bare + rich + COMPARE  
- [ ] ≥2 analysis scenarios  
- [ ] flow #3 digest  
- [ ] PROTOCOL заполнен (between-subject, N plan, Z, свой artifact)  

**Pass:** все.  
**Rework:** within-subject или нет PROTOCOL.

---

## Эталон pointer

[`05-bare-vs-rich-context-pack.md`](../instructor/rhythm-exemplars/05-bare-vs-rich-context-pack.md): покажите outline pitfalls и COMPARE-структуру.  
Runner README — подготовка к Н7, не обязательный прогон на Н6.

---

## Время на проверку

≈ **12–15 мин**: COMPARE → PROTOCOL (design fields) → digest файл.
