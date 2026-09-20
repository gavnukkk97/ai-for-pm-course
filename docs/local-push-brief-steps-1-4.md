# Local push brief — steps 1–4 (consolidated)

**Один paste локальному агенту.** Сводит handoff-ветки sequential production в `ai-for-pm-course` **main**, затем удаляет handoff.

Cloud agent **не** пишет в `gavnukkk97/ai-for-pm-course` (403). Работа — на машине kir.

Не redesign программы. Не трогать private Mail/Ya.

---

## Цель

Синхронизировать в публичный курс всё, что ещё лежит в handoff:

| Step | Handoff branch | Что внутри |
|---|---|---|
| 1 | `handoff/ai-for-pm-course-lectures` | `week-*/lecture.md` + README |
| 2 | `handoff/ai-for-pm-course-homework` | `week-*/homework.md` + `homework-key.md` + README |
| 3 | `handoff/ai-for-pm-course-slides` | `week-*/slides.md` + README |
| 4 | `handoff/ai-for-pm-course-p2` | examples S5 · unit-sheet · briefs mermaid · shot-list · indexes / QA / briefs |

Опционально ранее: `handoff/ai-for-pm-course-v2` (если main ещё без exemplars/n8n#2#3/runner/playbook) — см. [`local-push-brief.md`](./local-push-brief.md).

**Target:** https://github.com/gavnukkk97/ai-for-pm-course  
**Handoff repo:** https://github.com/gavnukkk97/product-analytics-ai-course

---

## Рекомендуемый порядок (один pass)

1. Clone/pull `ai-for-pm-course` main.  
2. По очереди checkout каждой handoff-ветки sibling-репо и `rsync`/`cp` `_handoff/ai-for-pm-course/` → target.  
3. Один commit на шаг *или* один большой commit в конце.  
4. Push main.  
5. Smoke.  
6. Удалить handoff-ветки.

Альтернатива: если Context/store доступен — копировать из store по отдельным briefs (`local-push-brief-lectures.md` … `local-push-brief-p2.md`) без handoff.

---

## Script (handoff → main)

```bash
set -euo pipefail

WORK="${TMPDIR:-/tmp}/ai-for-pm-sync-$$"
mkdir -p "$WORK" && cd "$WORK"

git clone https://github.com/gavnukkk97/ai-for-pm-course.git
cd ai-for-pm-course && git checkout main && git pull origin main
REPO="$(pwd)"
cd "$WORK"

git clone https://github.com/gavnukkk97/product-analytics-ai-course.git handoff-repo
cd handoff-repo

apply_handoff () {
  local branch="$1"
  local msg="$2"
  git fetch origin "$branch"
  git checkout "$branch"
  local HANDOFF="$(pwd)/_handoff/ai-for-pm-course"
  test -d "$HANDOFF"
  rsync -a "$HANDOFF/" "$REPO/"
  cd "$REPO"
  git add -A
  git status
  git commit -m "$msg" || echo "(nothing to commit for $branch)"
  cd "$WORK/handoff-repo"
}

# Order matters if files overlap (README): last write wins — apply p2 last.
apply_handoff handoff/ai-for-pm-course-lectures "Add lecture scripts weeks 0–8 (step 1/4)"
apply_handoff handoff/ai-for-pm-course-homework "Add homework packs weeks 0–8 (step 2/4)"
apply_handoff handoff/ai-for-pm-course-slides "Add slide decks weeks 0–8 (step 3/4)"
apply_handoff handoff/ai-for-pm-course-p2 "Add P2 pack: sample S5, unit-sheet, brief mermaids (step 4/4)"

cd "$REPO"
git push origin main
```

Если какая-то ветка уже влита — соответствующий `commit` будет пустым (ok).

---

## Smoke после push

- [ ] `docs/course/week-00…08/{lecture,homework,homework-key,slides,student-brief}.md`  
- [ ] `docs/course/sul/examples/s5-rhythm-filled-rubric.md` (EXAMPLE)  
- [ ] `docs/course/sul/templates/unit-sheet/*.csv`  
- [ ] `docs/course/instructor/screencast-cursor-10min-shotlist.md`  
- [ ] `docs/course/README.md` показывает steps 1–4 **done**  
- [ ] Нет секретов / private clouds  

---

## Удалить handoff-ветки (после успешного smoke)

```bash
cd "$WORK/handoff-repo"
git checkout main
for b in \
  handoff/ai-for-pm-course-lectures \
  handoff/ai-for-pm-course-homework \
  handoff/ai-for-pm-course-slides \
  handoff/ai-for-pm-course-p2
do
  git push origin --delete "$b" || true
done
# optional, if v2 already merged:
# git push origin --delete handoff/ai-for-pm-course-v2 || true
```

Локальные ветки/клоны `$WORK` можно стереть.

---

## Отдельные briefs (если нужен только один шаг)

| Step | Brief |
|---|---|
| 1 | [`local-push-brief-lectures.md`](./local-push-brief-lectures.md) |
| 2 | [`local-push-brief-homework.md`](./local-push-brief-homework.md) |
| 3 | [`local-push-brief-slides.md`](./local-push-brief-slides.md) |
| 4 | [`local-push-brief-p2.md`](./local-push-brief-p2.md) |
| v2 kit | [`local-push-brief.md`](./local-push-brief.md) |

---

## Остаток после sync

- **Авторский** RU-скринкаст Cursor (~10 мин) по [`docs/course/instructor/screencast-cursor-10min-shotlist.md`](./course/instructor/screencast-cursor-10min-shotlist.md) — единственный открытый P2-видео-gap.
