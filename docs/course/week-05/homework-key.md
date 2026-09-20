# Н5 · Ключ / рубрика преподавателя

**Студенту не выдавать целиком.** Выдача: [`homework.md`](./homework.md).  
**Эталон структуры:** [`../instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md`](../instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md).  
**Playbook:** [`../instructor/playbook-0-8.md`](../instructor/playbook-0-8.md) §Н5.

---

## Что выглядит хорошо

| Артефакт | Структура | Quality bar |
|---|---|---|
| DEFINITIONS | формула + окно + дедуп + source | Агент не «утверждает» определения |
| Дерево | NS → драйверы → рычаги | Связи, не KPI-список; H__ привязаны |
| Unit | одна единица ценности | UNKNOWN + план замера вместо выдуманного CAC |
| Scenarios | Downside/Base/Upside | Итог на NS или margin |
| CALIBRATION | ≥2 ручные правки | Студент объясняет, *где* агент врал |

**Отлично:** те же допущения, что tornado Н4, явно согласованы; Z для S4 назван.  
**Достаточно:** дерево + unit с UNKNOWN + калибровка.  
**Недостаточно:** числа Ритма вставлены в чужой продукт; нет калибровки.

---

## Частые провалы

| Симптом | Ремедиация |
|---|---|
| KPI-список без связей | «Что двигает NS?» → перерисовать дерево |
| Выдуманный CAC | Секция UNKNOWN + план |
| Агент «утвердил» модель | Требовать CALIBRATION.md |
| Скопированы числа Ритма | Свои; эталон только структура |
| Нет стыка с H__/tornado | Одна таблица соответствий |
| Слишком глубокое дерево | 4–8 драйверов достаточно |

---

## Чеклист оценки

- [ ] DEFINITIONS с формулами  
- [ ] Дерево со связями  
- [ ] Unit + UNKNOWN если нужно  
- [ ] 3 сценария  
- [ ] CALIBRATION (≥2 правки)  
- [ ] Стык с H__ или tornado  

**Pass:** все обязательные файлы + калибровка.  
**Rework:** нет калибровки или чужие числа без меток.

---

## Эталон pointer

[`04-metrics-tree-unit-sheet.md`](../instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md): покажите глубину NS→$ и блок калибровки («агент завысил CAC»). Не раздавайте готовые цифры как ответ.

Spreadsheet: [`../sul/templates/unit-sheet/`](../sul/templates/unit-sheet/) (CSV → Excel/Sheets по README). MD-таблица в сдаче тоже ок.

---

## Время на проверку

≈ **10–12 мин**: DEFINITIONS 3 строки → tree mermaid → CALIBRATION.
