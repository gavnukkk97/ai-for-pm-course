# Local push brief — для kir (вставить локальному агенту)

**Готово к копипасту.** Cloud agent **не** имеет write на `gavnukkk97/ai-for-pm-course` (ожидаемый 403). Синк — с машины kir.

---

## Цель

Синхронизировать материалы курса из Project store в публичный репозиторий:

**https://github.com/gavnukkk97/ai-for-pm-course**

Не ломать уже существующую студенческую структуру (`docs/course/week-00`, `week-01`, SUL S0). Мержить аддитивно: week-02…08, SUL S1–S5 templates, instructor pack, n8n #2/#3, runners, обновлённые индексы.

Сетку программы **не** переписывать.

---

## Source (Project store)

Корень Context:

`/cursor/stores/bc-31d1ec65-12ad-4994-b25c-a78ba5d9b56f/`

(На локальной машине kir путь может быть через Cursor Project / Context sync — взять актуальный checkout store.)

### Точные пути скопировать

| Store path | → Repo path | Note |
|---|---|---|
| `docs/course/` **целиком** | `docs/course/` | Включая `week-00…08`, `sul/`, `instructor/`, `README.md`, `materials-by-module.md` |
| `docs/ai-for-pm-course-program.md` | `docs/program.md` | В репо уже `docs/program.md` — **заменить/смержить** содержимым store (программа locked) |
| `docs/external-materials.md` | `docs/external-materials.md` | |
| `docs/course-qa-report.md` | `docs/course-qa-report.md` | создать, если нет |
| `docs/local-push-brief.md` | опц. `docs/local-push-brief.md` или не коммитить | этот бриф |

**Не обязательно** в публичный репо: `internal/`, `notes.md`, `materials-snapshots/` (если тяжёлые — по желанию kir).

Опциональный git bundle (полный tree store `docs/course` + program files):  
[`../internal/ai-for-pm-course-full.bundle`](../internal/ai-for-pm-course-full.bundle) — **готов** (~139KB, verified).

---

## Проверить layout на GitHub (сначала)

```bash
git clone https://github.com/gavnukkk97/ai-for-pm-course.git
cd ai-for-pm-course
git pull origin main
find docs -maxdepth 3 -type d | head -80
```

Ожидаемое (на момент cloud QA):

```text
docs/
  program.md
  external-materials.md
  course/
    README.md
    materials-by-module.md
    week-00/ … week-01/     ← уже есть
    sul/                    ← S0 (+ возможно частично)
```

После синка должны появиться / обновиться:

```text
docs/course/week-02 … week-08/
docs/course/instructor/playbook-0-8.md
docs/course/instructor/rhythm-exemplars/
docs/course/sul/n8n/flow-02-*, flow-03-*
docs/course/sul/runners/
docs/course/sul/templates/ (S3–S5)
docs/course/sul/personas/persona-bank-guide.md
docs/course/sul/hypotheses/hypothesis-runner-stub.md
docs/course-qa-report.md
```

---

## Merge rules (не удалять студенческое)

1. **Не** `git clean -fd` по `docs/course`.  
2. Копировать store → repo с перезаписью *одинаковых* путей (week packs / README / materials-by-module / sul README).  
3. Сохранить любые локальные правки kir, если новее (diff перед commit).  
4. Не коммитить секреты / API keys / private Mail.ru·Яндекс.  
5. `program.md` ← содержимое `ai-for-pm-course-program.md` (имя файла в репо — `program.md`).

Пример безопасного копирования (macOS/Linux):

```bash
STORE="…/bc-31d1ec65-12ad-4994-b25c-a78ba5d9b56f"   # поправить путь
REPO="…/ai-for-pm-course"

# course tree
rsync -a --delete --exclude '.DS_Store' \
  "$STORE/docs/course/" "$REPO/docs/course/"

# program rename
cp "$STORE/docs/ai-for-pm-course-program.md" "$REPO/docs/program.md"
cp "$STORE/docs/external-materials.md" "$REPO/docs/external-materials.md"
cp "$STORE/docs/course-qa-report.md" "$REPO/docs/course-qa-report.md"
```

`--delete` только внутри `docs/course/` — чтобы убрать устаревшие stubs; **не** применять к корню репо.

---

## Commit / push

Suggested message:

```text
Add weeks 2–8, SUL S1–S5 templates, Rhythm exemplars, n8n #2/#3, S4 runner, instructor playbook (v2)
```

```bash
cd "$REPO"
git checkout main
git status
git add docs/
git commit -m "Add weeks 2–8, SUL S1–S5 templates, Rhythm exemplars, n8n #2/#3, S4 runner, instructor playbook (v2)"
git push origin main
```

Если предпочтителен review: ветка `docs/v2-course-materials` + PR в `main` (на усмотрение kir).

---

## Bundle (альтернатива rsync)

Если store недоступен локально, взять bundle из Context:

`internal/ai-for-pm-course-full.bundle`

```bash
mkdir -p /tmp/ai-for-pm-from-bundle && cd /tmp/ai-for-pm-from-bundle
git clone "$STORE/internal/ai-for-pm-course-full.bundle" course-docs
# внутри — docs/course, docs/program.md, etc.
# затем rsync в клон gavnukkk97/ai-for-pm-course как выше
```

---

## Smoke после push

- [ ] `docs/course/week-08/checklist.md` открывается  
- [ ] `docs/course/sul/n8n/flow-02-signals-to-digest.json` import shape ok  
- [ ] `docs/course/sul/runners/README.md` + sample REPORT  
- [ ] `docs/course/instructor/playbook-0-8.md`  
- [ ] `docs/program.md` содержит 8-недельную сетку (не redesign)  
- [ ] Нет API keys в JSON n8n (`REPLACE_IN_N8N_UI` only)

---

## Cloud push attempt

Из VM cloud agent push в этот репо даёт **403** (`cursor[bot]` без write). Не блокер — этот бриф = основной путь.
