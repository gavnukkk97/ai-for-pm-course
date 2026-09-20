# Н3 · Ключ / рубрика преподавателя

**Студенту не выдавать целиком.** Выдача: [`homework.md`](./homework.md).  
**Эталон структуры:** [`../instructor/rhythm-exemplars/02-discovery-brief.md`](../instructor/rhythm-exemplars/02-discovery-brief.md).  
**n8n:** [`../sul/n8n/flow-02-description.md`](../sul/n8n/flow-02-description.md).  
**Playbook:** [`../instructor/playbook-0-8.md`](../instructor/playbook-0-8.md) §Н3.

---

## Что выглядит хорошо

| Артефакт | Структура | Quality bar |
|---|---|---|
| S1 | ≥15 / ≥3 segment | INDEX без дыр; сегменты различны по JTBD |
| Гипотеза | X→Y→Z + variants + artifact + red-team | Z = событие/метрика с определением; не engagement-only |
| Runner-plan | шаблон без дыр | between-subject; метрика до прогона |
| BRIEF | Минто ≤1 стр. | Есть абзац «не узнаем без живых» |
| Digest #2 | файл в `runs/n8n/` | Не рерайт ICP; top-5 сигналов + дыры |

**Отлично:** 1 runner-plan уже готов к S4 (N, seed, success event).  
**Достаточно:** 5 гипотез с Z и red-team; digests вручную скопирован.  
**Недостаточно:** «улучшим UX»; within-subject в плане.

---

## Частые провалы

| Симптом | Ремедиация |
|---|---|
| Engagement без Z | «Какое *событие* считаем успехом?» |
| Агент видит оба варианта | Запрет within-subject; показать AgentA/B |
| Digest = рерайт ICP | Дать inbox с 3 сырыми сигналами |
| <15 персон | Gate: не принимать S2 без S1 |
| Гипотезы не про свой продукт | Вернуть к ONEPAGER/artifact |
| LLM-оптимизм paywall | Red-team: цена ошибки + альтернатива «ничего» |

---

## Чеклист оценки

### Gates
- [ ] S1 ≥15 / ≥3  
- [ ] 5–7 H__ по шаблону  
- [ ] ≥1 runner-plan  
- [ ] BRIEF + REDTEAM/evidence  
- [ ] flow #2 digest в git  

**Pass:** все gates.  
**Partial:** S1 ok + гипотезы ok, digest mock — отметить follow-up.  
**Fail:** дырявая Z или within-subject.

---

## Эталон pointer

В [`02-discovery-brief.md`](../instructor/rhythm-exemplars/02-discovery-brief.md) покажите: ответ сверху → 3 аргумента → H__ одной строкой → «не узнаем». Не раздавайте заполненные H01–H03 Ритма как шаблон текста — только каркас.

---

## Время на проверку

≈ **12–18 мин**: INDEX count → 2 гипотезы на Z → BRIEF последняя секция → digest файл.
