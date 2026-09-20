# AI для продакта

Курс для продактов и аналитиков: собрать **AI-контур** (harness + n8n) и **Synthetic User Lab (SUL)** на своём продукте — с обязательной человеческой приёмкой.

Прошлые курсы учат *считать и решать по данным*. Этот — *делегировать research → гипотезы → экономику → претест → питч* агентам, не снимая ответственность с человека.

---

## Что вы получите

К концу 8 недель у вас будет:

1. **Рабочий AI-экзоскелет** — fluency ≥1 harness (Cursor или Claude Code) + skills + evals-lite.  
2. **n8n в ядре** — workflow’ы под продуктовые процессы (не SMM-автопостинг).  
3. **SUL S0→S5** на своём продукте: персоны → гипотезы → market sizing → претест ≥50–100 агентов → честная защита.  
4. **Портфель артефактов** — ICP, discovery briefs, strategy memo, дерево метрик, питч, decision memo.

Демо преподавателей идут на стенде **Ритм**; вы сдаёте **свой** продукт / рабочий кейс.

---

## Кому курс

- Продакты и аналитики с базой по метрикам / юниту / АБ (или эквивалент).  
- Код писать не обязательно; нужны терминал/файлы и доступ к своему продукту (или чёткому кейсу автоматизации).

**Не входит:** повтор JTBD/юнит/АБ «с нуля», промпт-сборник, контент-завод в Telegram.

---

## Как пройти (путь студента)

```text
Н0 env → Н1 harness+n8n+S0 → Н2 ICP/S1 → Н3 discovery/S2
     → Н4 ставки/S3 → Н5 метрики → Н6 analytics/S4 → Н7 питч/S4 → Н8 защита/S5
```

| Шаг | Что открыть первым | Зачем |
|---|---|---|
| 1 | Этот README | карта курса |
| 2 | [`docs/course/cold-start-triage.md`](docs/course/cold-start-triage.md) | ветки: live / idea-only / NDA / no-Docker |
| 3 | [`docs/course/README.md`](docs/course/README.md) | индекс недель и файлов |
| 4 | [`docs/course/week-00/`](docs/course/week-00/) → `student-brief.md` | старт онбординга |
| 5 | Каждую неделю: **brief → homework → checklist** | практика и приёмка |
| 6 | [`docs/course/sul/`](docs/course/sul/) | флагман SUL параллельно Н1–Н8 |

**Cold-start:** нет URL, NDA или нет Docker — не стоп. Сначала триаж → [`docs/course/cold-start-triage.md`](docs/course/cold-start-triage.md): что делаете каждую неделю и что заменяете.

Подробная программа (зафиксирована): [`docs/program.md`](docs/program.md).

---

## Карта недель

| Неделя | Тема | Старт для студента |
|---|---|---|
| [Н0](docs/course/week-00/) | Онбординг: env, договор «AI ≠ вывод», 1-pager | [`student-brief.md`](docs/course/week-00/student-brief.md) |
| [Н1](docs/course/week-01/) | AI-экзоскелет + n8n + **S0** | [`student-brief.md`](docs/course/week-01/student-brief.md) |
| [Н2](docs/course/week-02/) | ICP / конкуренты / УТП → **S1** | [`student-brief.md`](docs/course/week-02/student-brief.md) |
| [Н3](docs/course/week-03/) | Discovery + Минто → **S2** | [`student-brief.md`](docs/course/week-03/student-brief.md) |
| [Н4](docs/course/week-04/) | AI-ставки / стратегия → **S3** | [`student-brief.md`](docs/course/week-04/student-brief.md) |
| [Н5](docs/course/week-05/) | Дерево метрик / юнит / сценарии | [`student-brief.md`](docs/course/week-05/student-brief.md) |
| [Н6](docs/course/week-06/) | Bare vs rich аналитика → **S4** | [`student-brief.md`](docs/course/week-06/student-brief.md) |
| [Н7](docs/course/week-07/) | Питч + претест → **S4** | [`student-brief.md`](docs/course/week-07/student-brief.md) |
| [Н8](docs/course/week-08/) | Капстоун / защита → **S5** | [`student-brief.md`](docs/course/week-08/student-brief.md) |

Reading list по модулям: [`docs/course/materials-by-module.md`](docs/course/materials-by-module.md).

---

## Структура репозитория

```text
docs/course/
├── week-00/ … week-08/   ← недели (brief, ДЗ, checklist, …)
├── sul/                  ← Synthetic User Lab (S0→S5)
├── cold-start-triage.md  ← ветки live / idea / NDA / no-Docker
├── monday-survival-checklist.md ← ритуал после курса
├── media/                ← манифест скринов (бинарники — от автора)
├── instructor/           ← playbook и эталоны (для преподавателей)
└── materials-by-module.md
docs/program.md           ← утверждённая программа
docs/external-materials.md
```

В каждой неделе для студента обычно достаточно:

- `student-brief.md` — что сделать  
- `homework.md` — домашнее задание  
- `checklist.md` — критерии приёмки  

Остальное (`lecture.md`, `slides.md`, `instructor-notes.md`, `homework-key.md`) — для занятий и проверки.

---

## С чего начать прямо сейчас

1. Отметьте ветку в [`docs/course/cold-start-triage.md`](docs/course/cold-start-triage.md) (live / idea / NDA / no-Docker).  
2. Откройте [`docs/course/week-00/student-brief.md`](docs/course/week-00/student-brief.md).  
3. Поднимите harness (≥1) и n8n (Docker **или** Cloud), напишите 1-pager своего продукта.  
4. На Н1 скопируйте каркас [`docs/course/sul/`](docs/course/sul/) в **своё** репо.

На GitHub достаточно читать markdown в браузере; для сдачи удобнее clone/fork своего рабочего репо и копировать туда каркас `sul/`. Файлы `docs/local-push-brief*.md` и `HANDOFF-README.md` — служебные для авторов, студенту не нужны.

Вопросы по сетке и анти-скоупу — в [`docs/program.md`](docs/program.md).

---

## Что дальше после курса

Еженедельный ритуал (n8n digest · один skill · одна SUL-гигиена): [`docs/course/monday-survival-checklist.md`](docs/course/monday-survival-checklist.md). Также в конце [`Н8`](docs/course/week-08/).
