# Unit sheet / metrics scenarios — шаблон (Н5)

Практический spreadsheet под brief [`../../../week-05/student-brief.md`](../../../week-05/student-brief.md) и эталон [`../../../instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md`](../../../instructor/rhythm-exemplars/04-metrics-tree-unit-sheet.md).

## Файлы

| Файл | Лист / смысл |
|---|---|
| [`definitions.csv`](./definitions.csv) | DEFINITIONS: метрика · формула · окно · дедуп · источник |
| [`funnel-unit.csv`](./funnel-unit.csv) | Воронка / unit economics на одну волну |
| [`scenarios.csv`](./scenarios.csv) | Downside / Base / Upside + итог |
| [`calibration.csv`](./calibration.csv) | Что агент завысил/занизил (ритуал калибровки) |

Числа в CSV — **учебный пример Ритм** (napkin). Студент подставляет **свои** числа или оставляет ячейки пустыми и заполняет.

## Как открыть

**Вариант A — Excel / Google Sheets / LibreOffice**

1. Создайте новую книгу.  
2. Импортируйте каждый CSV как отдельный лист (File → Import / Данные → Из текста).  
3. Кодировка: **UTF-8**. Разделитель: **запятая**.  
4. Сохраните как `.xlsx` у себя локально (в репо курса достаточно CSV).

**Вариант B — только CSV**

Откройте файлы в любом редакторе таблиц; сдайте zip из 4 CSV + короткий `metrics/README.md` со ссылкой на DEFINITIONS.

**Вариант C — Google Sheets одной командой** (если установлен [`csvkit`](https://csvkit.readthedocs.io/) — опционально): импорт по одному файлу через UI «File → Import → Upload».

## Стык с Н5

1. Сначала `definitions.csv` (агент не меняет формулы без diff).  
2. Затем `funnel-unit.csv` + дерево (mermaid в `metrics/tree.md`).  
3. Три сценария → `scenarios.csv`.  
4. Калибровка ≥2 правок → `calibration.csv`.

## Анти-паттерны

- Выдуманный CAC/LTV без строки в DEFINITIONS.  
- Сдача эталонных чисел Ритма как «своих».  
- Сценарии без колонки «что должно быть верно».
