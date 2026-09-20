# Local push brief — P2 (step 4/4)

**Готово к копипасту.** Cloud → `ai-for-pm-course` = **403**. Синк с машины kir или через handoff.

**Скоп:** sample S5 examples · unit-sheet CSV · updated briefs Н2–Н8 · screencast shot-list · indexes / QA.  
Не redesign программы. Для полного sync всех шагов 1–4 см. [`local-push-brief-steps-1-4.md`](./local-push-brief-steps-1-4.md).

---

## Цель

Добавить P2-артефакты в:

**https://github.com/gavnukkk97/ai-for-pm-course**

---

## Source A — Project store

Корень: `/cursor/stores/bc-31d1ec65-12ad-4994-b25c-a78ba5d9b56f/`

```bash
STORE="…/bc-31d1ec65-12ad-4994-b25c-a78ba5d9b56f"
REPO="…/ai-for-pm-course"

# Examples S5
mkdir -p "$REPO/docs/course/sul/examples"
cp -R "$STORE/docs/course/sul/examples/." "$REPO/docs/course/sul/examples/"

# Unit-sheet
mkdir -p "$REPO/docs/course/sul/templates/unit-sheet"
cp -R "$STORE/docs/course/sul/templates/unit-sheet/." "$REPO/docs/course/sul/templates/unit-sheet/"

# Briefs + keys + indexes
for w in 02 03 04 05 06 07 08; do
  cp "$STORE/docs/course/week-$w/student-brief.md" "$REPO/docs/course/week-$w/student-brief.md"
done
cp "$STORE/docs/course/week-05/homework-key.md" "$REPO/docs/course/week-05/homework-key.md"
cp "$STORE/docs/course/week-08/homework-key.md" "$REPO/docs/course/week-08/homework-key.md"
cp "$STORE/docs/course/sul/README.md" "$REPO/docs/course/sul/README.md"
cp "$STORE/docs/course/README.md" "$REPO/docs/course/README.md"
cp "$STORE/docs/course/materials-by-module.md" "$REPO/docs/course/materials-by-module.md"
cp "$STORE/docs/course/instructor/rhythm-exemplars/README.md" "$REPO/docs/course/instructor/rhythm-exemplars/README.md"
cp "$STORE/docs/course/instructor/screencast-cursor-10min-shotlist.md" "$REPO/docs/course/instructor/screencast-cursor-10min-shotlist.md"
cp "$STORE/docs/course-qa-report.md" "$REPO/docs/course-qa-report.md"
cp "$STORE/docs/local-push-brief-p2.md" "$REPO/docs/local-push-brief-p2.md"
cp "$STORE/docs/local-push-brief-steps-1-4.md" "$REPO/docs/local-push-brief-steps-1-4.md"
```

---

## Source B — handoff branch

**Repo:** `gavnukkk97/product-analytics-ai-course`  
**Branch:** `handoff/ai-for-pm-course-p2`  
**Path:** `_handoff/ai-for-pm-course/`

```bash
git clone https://github.com/gavnukkk97/product-analytics-ai-course.git
cd product-analytics-ai-course
git fetch origin handoff/ai-for-pm-course-p2
git checkout handoff/ai-for-pm-course-p2
HANDOFF="$(pwd)/_handoff/ai-for-pm-course"

git clone https://github.com/gavnukkk97/ai-for-pm-course.git
cd ai-for-pm-course && git checkout main && git pull origin main
REPO="$(pwd)"

rsync -a "$HANDOFF/docs/" "$REPO/docs/"

git add docs/
git commit -m "Add P2 pack: sample S5, unit-sheet CSV, brief mermaids (step 4/4)"
git push origin main
```

---

## Smoke

- [ ] `docs/course/sul/examples/s5-rhythm-filled-rubric.md` открывается, помечен EXAMPLE  
- [ ] `docs/course/sul/templates/unit-sheet/*.csv` + README  
- [ ] `week-02`…`week-08/student-brief.md` содержат mermaid  
- [ ] Нет API keys / Mail·Ya private  
- [ ] Видео скринкаста **может** отсутствовать (shot-list достаточно для P2 sync)

---

## Cloud status

Push `ai-for-pm-course` с cloud → 403. Handoff — fallback.
