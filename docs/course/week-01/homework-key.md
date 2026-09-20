# Н1 · Ключ / рубрика преподавателя

**Студенту не выдавать целиком.** Выдача: [`homework.md`](./homework.md).  
**Playbook:** [`../instructor/playbook-0-8.md`](../instructor/playbook-0-8.md) §Н1 · flow: [`../sul/n8n/flow-01-description.md`](../sul/n8n/flow-01-description.md).

---

## Что выглядит хорошо

| Контур | Структура | Quality bar |
|---|---|---|
| Harness | Rules читают ONEPAGER; запрет выдуманных метрик | Студент объясняет skill vs разовый промпт |
| Skill | STATUS.md обновлён с диска; ≥3 golden в evals | Пустой бэклог / все Done / нет owner — покрыты |
| n8n #1 | Trigger → normalize → LLM/mock → artifact | Execution успешен; текст про **их** продукт; credentials в UI |
| S0 | Папки + notice + README «Мой продукт» | Dry-run лог есть; нет «среднего пользователя» как готового банка |

**Отлично:** mock-ветка задокументирована (`MOCK_LLM`), если нет API.  
**Достаточно:** Manual trigger + копипаст output в git.  
**Недостаточно:** только скрины чата без файлов.

---

## Частые провалы

| Симптом | Ремедиация |
|---|---|
| Skill не пишет файл | Проверить путь skill + права; показать live на Ритме |
| API key в JSON | Удалить; placeholder credentials |
| n8n = автопостинг | Вне скоупа → вернуть к backlog→summary |
| Путают n8n и harness | Harness = агент в IDE; n8n = оркестрация триггеров |
| README без продукта | Вернуть блок «Мой продукт» |
| Персоны уже «Мария эффективная» | Рано для S1; если есть — вернуть на schema |

---

## Чеклист оценки

### Harness / skill (0–3)
- [ ] Rules на месте  
- [ ] STATUS.md от skill  
- [ ] ≥3 golden cases  

### n8n #1 (0–3)
- [ ] Успешный execution  
- [ ] Артефакт в git / описан  
- [ ] Без секретов  

### S0 (0–3)
- [ ] Папки по контракту  
- [ ] Notice + README  
- [ ] Dry-run  

**Pass:** ≥2 в каждом блоке и нет красных флагов из checklist.  
**Rework:** любой missing контур или ключи в git.

---

## Эталоны (pointer, не ответ)

- Демо backlog-status на файлах Ритма — лекция Н1 / playbook.  
- Эталон структуры flow — `sul/n8n/flow-01-*` (instructor показывает Execute).  
- Rhythm exemplars для Н1 нет — начинаются с Н2.

---

## Время на проверку

≈ **8–12 мин**: clone/zip → STATUS.md → flow01-last → sul/README.
