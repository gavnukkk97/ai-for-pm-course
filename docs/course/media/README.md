# Media pack · что положить в репо (kir)

В публичном репо **пока нет** бинарных скринов/видео — это сознательный gap, не баг вёрстки. Ниже — точный список файлов, которые автор курса может дропнуть без переписывания программы.

Студентам до появления файлов достаточно текстовых brief’ов и официальных install-доков.

Связанный сценарий видео: [`../instructor/screencast-cursor-10min-shotlist.md`](../instructor/screencast-cursor-10min-shotlist.md).

---

## Правила

1. **Не** генерировать фейковые UI-скрины. Только запись с реального Cursor / n8n / вашего стенда.  
2. Без API keys, `.env`, личных чатов, Mail/Ya private ops.  
3. Подписи (alt / caption) — **на русском**.  
4. После дропа: проставить ссылки в [`../materials-by-module.md`](../materials-by-module.md) §Н0–Н1 и при желании в week briefs.  
5. Форматы: PNG или WebP для статичных; MP4 или YouTube/unlisted для скринкаста.

---

## Видео (приоритет P0)

| Путь (предложение) | Caption / куда ссылаться | Источник |
|---|---|---|
| `docs/course/media/cursor-10min-onboarding.mp4` **или** URL в materials-by-module | RU-скринкаст «Cursor за ~10 мин» для Н0 | shot-list: [`screencast-cursor-10min-shotlist.md`](../instructor/screencast-cursor-10min-shotlist.md) |

Пока файла нет — в Н0 brief оставить ссылки на cursor.com / Claude quickstart (уже есть).

---

## Скрины (P0 · минимум для cold-start)

| Путь | Caption (RU) | Где сослаться |
|---|---|---|
| `docs/course/media/n0-cursor-agent-hello.png` | Cursor Agent: принятый diff, файл `notes/hello.md` на диске | Н0 brief §harness |
| `docs/course/media/n0-n8n-workflows-empty.png` | n8n: список Workflows с одним сохранённым пустым flow (local **или** Cloud) | Н0 brief §n8n · ДЗ |
| `docs/course/media/n1-n8n-flow01-canvas.png` | n8n canvas flow #1 (webhook → … → артефакт), без секретов в нодах | Н1 brief · `sul/n8n/flow-01-*` |
| `docs/course/media/n1-skill-skillmd.png` | Проводник: папка skill + открытый `SKILL.md` | Н1 brief §skill |

---

## Скрины (P1 · SUL / доверие)

| Путь | Caption (RU) | Где сослаться |
|---|---|---|
| `docs/course/media/sul-folder-tree.png` | Дерево папок SUL (personas / hypotheses / runs) после S0 | `sul/README.md` · `folder-contract.md` |
| `docs/course/media/s4-runner-report-head.png` | Верх `REPORT.md` демо-прогона (можно crop из `sul/runners/runs/demo-h02-landing-n60/`) | Н6–Н7 · S4 |
| `docs/course/media/rhythm-stand-tour.png` | Тур стенда **Ритм** (instructor-only демо; не выдавать как «продукт студента») | Н0 lecture / playbook |

---

## Опционально (P2)

| Путь | Caption |
|---|---|
| `docs/course/media/n0-claude-code-terminal.png` | Claude Code: terminal dry-run для dual-track |
| `docs/course/media/n8n-cloud-vs-docker.png` | Два окна/вкладки: Cloud URL vs local `:5678` — для ветки D cold-start |

---

## Чеклист после дропа

- [ ] Файлы лежат по путям выше (или обновить таблицу, если имена другие).  
- [ ] В markdown — изображение с путём вида `docs/course/media/….png` и осмысленным alt на русском.  
- [ ] Gap «RU-скринкаст Cursor» в materials-by-module → **filled**.  
- [ ] Этот README: отметить строки как landed (дата).

**Статус на 2026-09-20:** ни одного бинарного файла в `media/` ещё нет — только этот манифест.
