# Эталон · Prefest/pitch demo notes · Ритм (лендинг)

**Недели:** Н7 (питч + S4) · Н8 (talk-track защиты)  
**Артефакт:** два варианта **текста лендинга / paywall** Ритма (в репо prior course нет отдельного HTML-лендинга — используем UX-копию из уроков как SUL artifact).

Протокол: [`../../sul/templates/pretest-protocol.md`](../../sul/templates/pretest-protocol.md)  
Runner: [`../../sul/runners/`](../../sul/runners/) · sample REPORT: `../../sul/runners/runs/demo-h02-landing-n60/REPORT.md`

---

## A / B copy (artifact under test)

### Variant A — control («налог»)

```text
Ритм — привычки без хаоса.

Оформить Pro
Тарифы: от 299 ₽/мес
Продолжить
```

Цена легко теряется; CTA без явного обмена лимита.

### Variant B — treatment (benefit)

```text
Ритм — удержи 1–3 ритуала, не бросая через неделю.

Снять лимит: 3 привычки и напоминания
Pro — 299 ₽/мес или 1 990 ₽/год · отмена в один тап
```

Цена + benefit above fold (паттерн M1.6).

**Чем A≠B для пользователя:** понятность обмена «лимит ↔ деньги», не другой продукт.

---

## Дизайн претеста (эталон)

| Поле | Значение |
|---|---|
| H id | H02 |
| Design | **between-subject** |
| N | 60 (демо-лог) / live smoke 4–6 |
| Allocation | ~1:1 |
| Seed | `ritm-h02-20260918` |
| Primary | success rate (intent pay / clear value refusal ≠ confusion) |
| Blind | агент видит только свой variant |

Запрещено: один агент оценивает A и B; «выбери лучший».

---

## Питч стейкхолдеру (7 секций, ~6–7 мин)

1. **Контекст:** Ритм, ICP, bottleneck depth.  
2. **Ставка:** thin-bet на copy paywall до медиа.  
3. **Метод:** SUL between-subject N=60, seed, границы.  
4. **Результат:** направление эффекта + top themes (см. sample REPORT).  
5. **Не доказали:** живой WTP, каналы, смещение LLM.  
6. **Ask:** бюджет 2 недели живого теста креатива/онбординга.  
7. **Цена ошибки:** ship по синтетике vs упущенный тест.

ЛПР-brief для спарринга: «CPO маркетплейса привычек, ненавидит vanity metrics».

---

## Sample REPORT (ссылка)

Полный демо-отчёт генерируется runner’ом в mock-режиме:

`docs/course/sul/runners/runs/demo-h02-landing-n60/REPORT.md`

На занятии: live 2 персоны × assignment; полный N — с экрана готового лога.

---

## Talk-track S5 (6 мин, честный)

1. Дуга S0→S5 на Ритме одной минутой.  
2. Вердикт по H02: **supports direction** / по H01 кусок — **inconclusive** (намеренно).  
3. Слайд «где врёт»: LLM-осознанность, нет live UI, N=60 не мощность живого АБ.  
4. Калибровка: «знак совпал / не совпал с маленьким прошлым АБ стенда — сказать вслух».  
5. Next: живой тест; harness+n8n на работе.

Рубрика: реалистично **24–30 / 39**, не идеал — см. `sul/templates/s5-defense-rubric.md`.
