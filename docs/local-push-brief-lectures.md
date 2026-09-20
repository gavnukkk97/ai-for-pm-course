# Local push brief — лекции Н0–Н8 (paste локальному агенту)

**Готово к копипасту.** Cloud agent **не** имеет write на `gavnukkk97/ai-for-pm-course` (ожидаемый 403). Синк — с машины kir **или** через handoff-ветку sibling-репо.

**Скоп этого брифа:** только новые `lecture.md` + обновлённый `docs/course/README.md`. Не трогать homework/slides/P2 (их ещё нет). Не redesign программы.

---

## Цель

Добавить лекционные скрипты в публичный репозиторий:

**https://github.com/gavnukkk97/ai-for-pm-course**

---

## Source A — Project store (предпочтительно, если Context доступен)

Корень:

`/cursor/stores/bc-31d1ec65-12ad-4994-b25c-a78ba5d9b56f/`

| Store path | → Repo path |
|---|---|
| `docs/course/week-00/lecture.md` | `docs/course/week-00/lecture.md` |
| `docs/course/week-01/lecture.md` | `docs/course/week-01/lecture.md` |
| `docs/course/week-02/lecture.md` | `docs/course/week-02/lecture.md` |
| `docs/course/week-03/lecture.md` | `docs/course/week-03/lecture.md` |
| `docs/course/week-04/lecture.md` | `docs/course/week-04/lecture.md` |
| `docs/course/week-05/lecture.md` | `docs/course/week-05/lecture.md` |
| `docs/course/week-06/lecture.md` | `docs/course/week-06/lecture.md` |
| `docs/course/week-07/lecture.md` | `docs/course/week-07/lecture.md` |
| `docs/course/week-08/lecture.md` | `docs/course/week-08/lecture.md` |
| `docs/course/README.md` | `docs/course/README.md` |

Опционально рядом (не обязательно для шага 1): `docs/local-push-brief-lectures.md`.

```bash
STORE="…/bc-31d1ec65-12ad-4994-b25c-a78ba5d9b56f"
REPO="…/ai-for-pm-course"

for w in 00 01 02 03 04 05 06 07 08; do
  cp "$STORE/docs/course/week-$w/lecture.md" "$REPO/docs/course/week-$w/lecture.md"
done
cp "$STORE/docs/course/README.md" "$REPO/docs/course/README.md"
```

---

## Source B — handoff branch (если push в ai-for-pm-course с cloud = 403)

Тот же паттерн, что v2:

**Handoff repo:** `gavnukkk97/product-analytics-ai-course`  
**Branch (создаётся cloud-агентом при успехе):** `handoff/ai-for-pm-course-lectures`  
**Path inside:** `_handoff/ai-for-pm-course/docs/course/…`

```bash
git clone https://github.com/gavnukkk97/product-analytics-ai-course.git
cd product-analytics-ai-course
git fetch origin handoff/ai-for-pm-course-lectures
git checkout handoff/ai-for-pm-course-lectures
HANDOFF="$(pwd)/_handoff/ai-for-pm-course"

git clone https://github.com/gavnukkk97/ai-for-pm-course.git
cd ai-for-pm-course && git checkout main && git pull origin main
REPO="$(pwd)"

for w in 00 01 02 03 04 05 06 07 08; do
  mkdir -p "$REPO/docs/course/week-$w"
  cp "$HANDOFF/docs/course/week-$w/lecture.md" "$REPO/docs/course/week-$w/lecture.md"
done
cp "$HANDOFF/docs/course/README.md" "$REPO/docs/course/README.md"

git add docs/course/week-*/lecture.md docs/course/README.md
git commit -m "Add lecture scripts for weeks 0–8 (step 1/4 materials)"
git push origin main
```

Если ветка handoff ещё не появилась — копировать **Source A** (store paths выше) вручную из Cursor Context.

---

## Smoke после push

- [ ] `docs/course/week-00/lecture.md` … `week-08/lecture.md` открываются  
- [ ] В `docs/course/README.md` есть таблица «Лекции по неделям»  
- [ ] Нет API keys / private Mail·Ya в файлах  
- [ ] Homework/slides **не** появились случайно (шаг 1 только лекции)

---

## Cloud status

Попытка push в `ai-for-pm-course` с cloud → **403** (как раньше). Handoff в `product-analytics-ai-course` — fallback; не блокер доставки в Project store.
