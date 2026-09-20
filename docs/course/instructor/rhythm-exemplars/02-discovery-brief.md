# Эталон · Discovery brief (Минто) · Ритм

**Неделя:** Н3 · instructor demo  
Связь: [`01-icp-competitive-map.md`](./01-icp-competitive-map.md) · шаблон гипотез `sul/hypotheses/_TEMPLATE.md`

---

## BRIEF.md (≤1 стр.)

### Ответ сверху

Главная проблема ICP Ритма: люди **создают привычку**, но не доходят до **D7 depth ≥3**; early paywall давит до value → ложный сигнал «дорого», хотя узкое место — depth, не цена.

### Три аргумента

1. Воронка стенда: habit→depth ≈ **27%** — bottleneck; paywall reach часто > depth.  
2. Анти-ICP отсечён: не чиним корпоративный wellness и каталог из 50 привычек.  
3. Синтетический претест копий лендинга/paywall дешевле живого трафика, но **не** ship/kill.

### Портфель гипотез (строки)

| Id | Одна строка |
|---|---|
| H01 | Перенос paywall после streak_3 → ↑ depth, guardrail ↓ early pressure |
| H02 | Benefit-copy на лендинге/paywall («снять лимит 3 привычки») → ↑ trial/pay intent vs «Оформить Pro» |
| H03 | Укороченный онбординг (цель «3 дня», без карусели) → ↑ D1 check-in |

### Чего не узнаем без живых людей

Реальный WTP, креатив-усталость каналов, эффект App Store рейтинга, смещение LLM к «осознанности».

---

## Три гипотезы X→Y→Z (эталон разбора)

### H01 — timing paywall

| Поле | Значение |
|---|---|
| X | Показ paywall в основном после `streak_3_reached` (treatment) vs early (control) |
| Y | Пользователь успевает почувствовать value до просьбы о деньгах |
| Z | Доля `habit_created` → `depth≥3` за 7д; знаменатель = users с `habit_created` в когорте; дедуп по `user_id`; окно 7д от habit |
| Guardrail | Early paywall share; subscribe_14d не падает >X pp без объяснения |
| Artifact A/B | CJM ветки early vs late (текст/скрин демо) |
| Red-team | 1) LLM любит «отложить paywall» → ложный supports · 2) артефакт ≠ живой UI |

### H02 — benefit copy (лендинг / paywall)

| Поле | Значение |
|---|---|
| X | CTA «Снять лимит: 3 привычки и напоминания» + цена above fold vs «Оформить Pro» без цены |
| Y | Понятен обмен: лимит freemium ↔ деньги |
| Z | Success = агент доходит до intent pay / явного «готов платить» **или** отказ с причиной про ценность (не «не понял цену»); primary для претеста Н7 — conversion-proxy `success` на варианте |
| Artifact | Два текста лендинга (см. [`06-pretest-pitch-demo-notes.md`](./06-pretest-pitch-demo-notes.md)) |
| Red-team | 1) within-subject «выбери лучший» запрещён · 2) скрин без цены ≠ live |

### H03 — короткий онбординг

| Поле | Значение |
|---|---|
| X | Экран «Какую привычку держим?» + пример + CTA «Создать»; без success-карусели и 4 social buttons |
| Y | Time-to-first-habit ↓ → больше D1 check-in |
| Z | `onboarding_completed` → ≥1 `check_in` в D1; знаменатель = completed onboarding; окно 24ч |
| Red-team | Упрощение режет сегмент productivity-maxers, которым нужны 3 привычки сразу |

### Дырявая Z (для разбора на занятии)

«Увеличим engagement» — нет числителя, знаменателя, окна, дедупа → S2 не принимается.

---

## Evidence (демо-папка)

```text
evidence/
  inbox/   ← 3 заметки: desk bottleneck 27%; copy before/after M1.6; AgentA/B between-subject
  curated/ ← карточки факт→вывод→уверенность
  REDTEAM.md
```

n8n flow #2 собирает inbox → `runs/n8n/digest-*.md` — см. `sul/n8n/flow-02-*`.
