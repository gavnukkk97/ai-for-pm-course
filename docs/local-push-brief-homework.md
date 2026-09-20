# Local push brief — homework Н0–Н8 (paste локальному агенту)

**Готово к копипасту.** Cloud agent **не** имеет write на `gavnukkk97/ai-for-pm-course` (ожидаемый 403). Синк — с машины kir **или** через handoff-ветку sibling-репо.

**Скоп этого брифа:** `homework.md` + `homework-key.md` по `week-00`…`week-08` + обновлённый `docs/course/README.md`. Не трогать slides/P2 (их ещё нет). Не redesign программы. Лекции уже должны быть на main (или синкнуть отдельно по [`local-push-brief-lectures.md`](./local-push-brief-lectures.md)).

---

## Цель

Добавить homework packs (+ instructor keys) в публичный репозиторий:

**https://github.com/gavnukkk97/ai-for-pm-course**

---

## Source A — Project store (предпочтительно, если Context доступен)

Корень:

`/cursor/stores/bc-31d1ec65-12ad-4994-b25c-a78ba5d9b56f/`

| Store path | → Repo path |
|---|---|
| `docs/course/week-00/homework.md` | `docs/course/week-00/homework.md` |
| `docs/course/week-00/homework-key.md` | `docs/course/week-00/homework-key.md` |
| `docs/course/week-01/homework.md` | `docs/course/week-01/homework.md` |
| `docs/course/week-01/homework-key.md` | `docs/course/week-01/homework-key.md` |
| `docs/course/week-02/homework.md` | `docs/course/week-02/homework.md` |
| `docs/course/week-02/homework-key.md` | `docs/course/week-02/homework-key.md` |
| `docs/course/week-03/homework.md` | `docs/course/week-03/homework.md` |
| `docs/course/week-03/homework-key.md` | `docs/course/week-03/homework-key.md` |
| `docs/course/week-04/homework.md` | `docs/course/week-04/homework.md` |
| `docs/course/week-04/homework-key.md` | `docs/course/week-04/homework-key.md` |
| `docs/course/week-05/homework.md` | `docs/course/week-05/homework.md` |
| `docs/course/week-05/homework-key.md` | `docs/course/week-05/homework-key.md` |
| `docs/course/week-06/homework.md` | `docs/course/week-06/homework.md` |
| `docs/course/week-06/homework-key.md` | `docs/course/week-06/homework-key.md` |
| `docs/course/week-07/homework.md` | `docs/course/week-07/homework.md` |
| `docs/course/week-07/homework-key.md` | `docs/course/week-07/homework-key.md` |
| `docs/course/week-08/homework.md` | `docs/course/week-08/homework.md` |
| `docs/course/week-08/homework-key.md` | `docs/course/week-08/homework-key.md` |
| `docs/course/README.md` | `docs/course/README.md` |

Опционально рядом: `docs/local-push-brief-homework.md`.

```bash
STORE="…/bc-31d1ec65-12ad-4994-b25c-a78ba5d9b56f"
REPO="…/ai-for-pm-course"

for w in 00 01 02 03 04 05 06 07 08; do
  cp "$STORE/docs/course/week-$w/homework.md" "$REPO/docs/course/week-$w/homework.md"
  cp "$STORE/docs/course/week-$w/homework-key.md" "$REPO/docs/course/week-$w/homework-key.md"
done
cp "$STORE/docs/course/README.md" "$REPO/docs/course/README.md"
```

---

## Source B — handoff branch (если push в ai-for-pm-course с cloud = 403)

Тот же паттерн, что lectures/v2:

**Handoff repo:** `gavnukkk97/product-analytics-ai-course`  
**Branch (создаётся cloud-агентом при успехе):** `handoff/ai-for-pm-course-homework`  
**Path inside:** `_handoff/ai-for-pm-course/docs/course/…`

```bash
git clone https://github.com/gavnukkk97/product-analytics-ai-course.git
cd product-analytics-ai-course
git fetch origin handoff/ai-for-pm-course-homework
git checkout handoff/ai-for-pm-course-homework
HANDOFF="$(pwd)/_handoff/ai-for-pm-course"

git clone https://github.com/gavnukkk97/ai-for-pm-course.git
cd ai-for-pm-course && git checkout main && git pull origin main
REPO="$(pwd)"

for w in 00 01 02 03 04 05 06 07 08; do
  mkdir -p "$REPO/docs/course/week-$w"
  cp "$HANDOFF/docs/course/week-$w/homework.md" "$REPO/docs/course/week-$w/homework.md"
  cp "$HANDOFF/docs/course/week-$w/homework-key.md" "$REPO/docs/course/week-$w/homework-key.md"
done
cp "$HANDOFF/docs/course/README.md" "$REPO/docs/course/README.md"

git add docs/course/week-*/homework.md docs/course/week-*/homework-key.md docs/course/README.md
git commit -m "Add homework packs and keys for weeks 0–8 (step 2/4 materials)"
git push origin main
```

Если ветка handoff ещё не появилась — копировать **Source A** (store paths выше) вручную из Cursor Context.

---

## Smoke после push

- [ ] `docs/course/week-00/homework.md` … `week-08/homework.md` открываются  
- [ ] `docs/course/week-00/homework-key.md` … `week-08/homework-key.md` открываются  
- [ ] В `docs/course/README.md` есть таблица «Домашние задания (+ ключи)»  
- [ ] Нет API keys / private Mail·Ya в файлах  
- [ ] Slides/P2 **не** появились случайно (шаг 2 только homework)

---

## Cloud status

Попытка push в `ai-for-pm-course` с cloud → **403** (как раньше). Handoff в `product-analytics-ai-course` — fallback; не блокер доставки в Project store.
