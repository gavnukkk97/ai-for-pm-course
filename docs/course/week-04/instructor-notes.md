# Н4 · Instructor notes — go/no-go memo на Ритме

## Цель демо (~35 мин)

Показать честный **thin-bet** на paywall Ритма: sizing снизу вверх + tornado, без «рынок $10B».

---

## Prep

- [ ] 3 сегмента Ритма с Н2.  
- [ ] Заранее посчитанный base case на листочке (чтобы не тупить в арифметике live).  
- [ ] Пустой `market-tornado` на экране.  
- [ ] Одна «плохая» ставка: «AI напишет весь маркетинг» — для red-team.

---

## Скрипт A — Ставки (10 мин)

1. Ставка 1 (хорошая): претест копий лендинга в SUL до закупки трафика.  
2. Ставка 2: агент-дайджест метрик paywall.  
3. Ставка 3 (убить): полная автономия ship без человека.  
4. Класс голосует kill на #3.

## Скрипт B — Bottom-up + tornado (20 мин)

1. Reach сегмента habit-starters: assumption 50k reachable RU, desk.  
2. Trial 8% → paid 4% → ARPU 299 ₽.  
3. Tornado: reach ±50%, trial ±3pp, price 199/299/499.  
4. Вывод: решение чувствительнее к trial, чем к цене → живой тест креатива/онбординга, не прайсинг первым.  
5. Заполнить memo: thin-bet на претест; no-go на авто-ship.

## Скрипт C — Границы (5 мин)

SSR/синтетика = intent proxy. Фраза на слайд из программы §3.4.

---

## Типичные сбои

| Симптом | Реакция |
|---|---|
| TAM сверху вниз из блога | Заменить на bottom-up от сегментов персон |
| Нет kill-критерия | Блокер memo |
| Ставки не связаны с H__ | Вернуть к портфелю Н3 |
| Tornado без источников допущений | Добавить колонку source |

---

## Ops

Не тянуть цифры из private clouds в студенческую выдачу.

---

## Эталоны / playbook

- **Эталон go/no-go memo:** [`../instructor/rhythm-exemplars/03-strategy-go-no-go-memo.md`](../instructor/rhythm-exemplars/03-strategy-go-no-go-memo.md)
- Playbook: [`../instructor/playbook-0-8.md`](../instructor/playbook-0-8.md)
