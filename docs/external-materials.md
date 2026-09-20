# Внешние материалы — AI для продакта

Кураторский список (YouTube / Medium / LinkedIn / GitHub / arXiv / RU-курсы).  
Снапшоты свободных текстов/PDF: [`materials-snapshots/`](./materials-snapshots/).  
Карта «лучший → модуль» также в [`ai-for-pm-course-program.md`](./ai-for-pm-course-program.md) §6.

Легенда **модулей:** Н1 экзоскелет · Н2 ICP/рынок · Н3 discovery · Н4 AI-ставки · Н5 метрики · Н6 аналитика-агент · Н7 питч · **SUL** флагман (синтетические пользователи).

---

## Топ-пики (приоритет для производства)

| # | Title | URL | Why useful | Module | Lang | Free/Paid | Downloadable |
|---|---|---|---|---|---|---|---|
| 1 | **phuryn/pm-skills** — 68 Claude skills / 9 plugins | https://github.com/phuryn/pm-skills | Готовые skills discovery→strategy→market research→analytics; идеальный каркас «AI-команды продакта» | Н1–Н5, Н7 | EN | Free (MIT) | Yes — README snapshot |
| 2 | **AgentA/B** (arXiv) | https://arxiv.org/abs/2504.09723 | Канон флагмана: LLM-персоны на живом сайте как претест до A/B | SUL, Н3–Н4 | EN | Free | Yes — PDF + abstract |
| 3 | **voice-of-agents** | https://github.com/blakeaber/voice-of-agents | Research→eval bridge, обязательный SYNTHETIC-DATA-NOTICE — этика SUL | SUL, Н2–Н3 | EN | Free (MIT) | Yes — README |
| 4 | **synthetic-market-research** + SSR | https://github.com/BayramAnnakov/synthetic-market-research · https://arxiv.org/abs/2510.08338 | Market sizing / purchase intent без «магического TAM»; free-text→Likert via SSR | Н4, SUL S3 | EN | Free | Yes — README + PDF |
| 5 | **SimAB** (arXiv) | https://arxiv.org/abs/2603.01024 | Симуляция A/B на скринах/вариантах; калибровка на 47 исторических тестах | SUL S4 | EN | Free | Yes — PDF |
| 6 | Claude for PMs (Huryn) — YouTube | https://www.youtube.com/watch?v=bITUsUsrxjM | Живой OS: Cowork + Code + skills + MCP; не промпты, а процессы | Н1 | EN | Free | Link only |
| 7 | Why PM care about Agent Harness (Medium) | https://medium.com/design-bootcamp/why-should-pm-care-about-agent-harness-5e4a5ae5a1ee | Язык занятия 1: harness = продукт (автономия, guardrails, evals) | Н1 | EN | Free* | Soft wall; no full snapshot |
| 8 | PM AI Agent Fleet / Discovery stack (Falk Gottlob) | https://medium.com/@falkgottlob/the-pm-ai-agent-fleet-39-agents-mapped-to-the-7-stage-operating-system-92b1b7065bba · https://medium.com/@falkgottlob/build-a-discovery-agent-stack-continuous-customer-listening-da8a71e601eb | Карта агентов по стадиям PM OS; discovery stack на практике | Н1–Н3 | EN | Free* | Soft wall |
| 9 | 6 способов AI в работе PM | https://www.youtube.com/watch?v=ET3z8wSNUiA | RU-вход: research, интервью, прототип, PRD, метрики | Н0–Н3 | RU | Free | Link only |
| 10 | ИИ-агенты как продукт (YouTube) | https://www.youtube.com/watch?v=Ieq8cY0UcHo | Агенты как продукт + skills + ошибки масштаба — тон Н4/Н7 | Н4, Н7 | RU | Free | Link only |
| 11 | AI Agents for Product Leaders (LinkedIn Learning, Marily Nika) | https://www.linkedin.com/learning/ai-agents-for-product-leaders | Короткий (29м) каркас: agentic products, ethics, launch | Н0, Н4 | EN | Paid (LI Learning) | No |
| 12 | Building synthetic users… (YouTube) | https://www.youtube.com/watch?v=b4MUT_NSq7M | Демо synthetic users для research | SUL, Н2 | EN | Free | Link only |
| 13 | **Cursor Agent Skills (docs)** | https://cursor.com/docs/skills | Офиц. контракт skills для Н1 (Cursor track) | Н1 | EN | Free | Yes — [`cursor-skills-docs.md`](./materials-snapshots/cursor-skills-docs.md) |
| 14 | **Claude Code — custom skills** | https://code.claude.com/docs/en/custom-skills | Офиц. skills + CLAUDE.md для Н1 (Claude track) | Н1 | EN | Free | Yes — snapshot |
| 15 | **n8n AI intro + Webhook + Read/Write File** | https://docs.n8n.io/advanced-ai/intro-tutorial/ · webhook · readwritefile | Ядро n8n flow #1 | Н1, SUL S0 | EN | Free | Yes — snapshots |
| 16 | **deanpeters/Product-Manager-Skills** | https://github.com/deanpeters/Product-Manager-Skills | Альтернатива/дополнение phuryn; 49 skills, Claude+Codex | Н1–Н5 | EN | Free (OSS) | Yes — README snapshot |
| 17 | **n8n blog: AI Agents Explained** | https://blog.n8n.io/ai-agents/ | Теория агентов → практика n8n (не SMM) | Н1 | EN | Free | Yes — excerpt |
| 18 | **Agent Skills specification** | https://agentskills.io/specification | Общий стандарт SKILL.md (Cursor/Claude) | Н1 | EN | Free | Yes — snapshot |

\*Medium часто открывается без логина, но полный офлайн-дамп нестабилен — храним ссылки.

---

## YouTube

| Title | URL | Why useful | Module | Lang | Free/Paid | Downloadable |
|---|---|---|---|---|---|---|---|
| 6 способов использовать AI в работе продакт-менеджера | https://www.youtube.com/watch?v=ET3z8wSNUiA | Практичные сценарии дня PM | Н0–Н3 | RU | Free | No (link) |
| Об ИИ-агентах как продукте, скиллах… | https://www.youtube.com/watch?v=Ieq8cY0UcHo | Агенты ≠ чат; навыки PM | Н4, Н7 | RU | Free | No |
| Complete Course: Claude for PMs (Cowork+Code+Dispatch) | https://www.youtube.com/watch?v=bITUsUsrxjM | Полный OS + pm-skills live | Н1 | EN | Free | No |
| Why Every PM Must Use Claude Code | https://www.youtube.com/watch?v=hLYK28IlvyE | Мотивация harness для PM | Н1 | EN | Free | No |
| How to Build an AI Agent with Claude Code | https://www.youtube.com/watch?v=bcM9dP_uXJU | Туториал агента | Н1 | EN | Free | No |
| Building synthetic users for advanced user research | https://www.youtube.com/watch?v=b4MUT_NSq7M | Synthetic users research | SUL | EN | Free | No |
| How to get real product feedback from synthetic users | https://www.youtube.com/watch?v=q_fdcbwHJKQ | Feedback loop на синтетике | SUL, Н3 | EN | Free | No |
| What are Synthetic Users? | https://www.youtube.com/watch?v=w-bZckedky8 | Intro-понятие | SUL | EN | Free | No |
| How I Use AI as a Product Manager | https://www.youtube.com/watch?v=KjYCEiBTHFo | Личный workflow PM | Н0 | EN | Free | No |
| Free webinar: AI-Native Product Manager (Product School) | https://www.youtube.com/watch?v=Xp_iIkt94TQ | Обзор AI-native PM | Н0 | EN | Free | No |
| How AI is reshaping the product role (Lenny / Udezue) | https://www.youtube.com/watch?v=e1R_-esuO9o | Сдвиг роли PM | Н0, Н4 | EN | Free | No |
| n8n Webhook Node Explained | https://www.youtube.com/watch?v=omzkPzQHS8k | Webhook → agent → respond (паттерн flow #1) | Н1 | EN | Free | No |
| Search: «ai для продакта» | https://www.youtube.com/results?search_query=ai+для+продакта | RU-выдача нестабильна в API; смотреть вручную | — | RU | Free | — |

**Не риповали видео** — только ссылки и заметки.

---

## Medium

| Title | URL | Why useful | Module | Lang | Free/Paid | Downloadable |
|---|---|---|---|---|---|---|---|
| Why should PM care about Agent Harness? | https://medium.com/design-bootcamp/why-should-pm-care-about-agent-harness-5e4a5ae5a1ee | Определения harness для занятия 1 | Н1 | EN | Free* | No full dump |
| The PM AI Agent Fleet (39 agents) | https://medium.com/@falkgottlob/the-pm-ai-agent-fleet-39-agents-mapped-to-the-7-stage-operating-system-92b1b7065bba | Карта агентов × стадии | Н1–Н7 | EN | Free* | No |
| Build a discovery agent stack | https://medium.com/@falkgottlob/build-a-discovery-agent-stack-continuous-customer-listening-da8a71e601eb | Стек continuous discovery | Н2–Н3 | EN | Free* | No |
| AI Agents For Product Managers | https://medium.com/@bhushannemade2001/ai-agents-for-product-managers-b2dfe10adf82 | Агенты по петле discovery→post-launch | Н1–Н6 | EN | Free* | Partial fetch |
| How I built a 14-agent product team (Claude Code) | https://medium.com/@ndbarrett/how-i-built-a-14-agent-product-team-13-sub-agents-plus-one-cpo-orchestrator-with-claude-code-b66709033465 | Orchestrator + quality gates | Н1, Н3 | EN | Free* | No |
| Turn Claude Into a PM: 100+ open-source skills | https://civillearning.medium.com/turn-claude-into-a-product-manager-100-open-source-pm-skills-you-can-install-today-b38fcd70389d | Обзор pm-skills команд | Н1–Н5 | EN | Free* | No |
| Product Compass — PM Skills Marketplace | https://www.productcompass.pm/p/pm-skills-marketplace-claude | Анонс/объяснение marketplace skills (Huryn) | Н1 | EN | Free article | Partial |

---

## Official docs (harness + n8n) — добор Sep 2026

| Title | URL | Why useful | Module | Lang | Free/Paid | Downloadable |
|---|---|---|---|---|---|---|
| Cursor Agent Skills | https://cursor.com/docs/skills | Skills dirs, SKILL.md frontmatter, vs rules | Н1 | EN | Free | [`cursor-skills-docs.md`](./materials-snapshots/cursor-skills-docs.md) |
| Cursor Rules | https://cursor.com/docs/rules | AGENTS.md / project rules | Н0–Н1 | EN | Free | Link |
| Claude Code Quickstart | https://code.claude.com/docs/en/quickstart | Установка CLI | Н0 | EN | Free | [`claude-code-quickstart.md`](./materials-snapshots/claude-code-quickstart.md) |
| Claude Code custom skills | https://code.claude.com/docs/en/custom-skills | SKILL.md для Claude track | Н1 | EN | Free | [`claude-code-custom-skills.md`](./materials-snapshots/claude-code-custom-skills.md) |
| Claude Code memory / CLAUDE.md | https://code.claude.com/docs/en/claude-md | Постоянный контекст проекта | Н1 | EN | Free | Link |
| Agent Skills spec | https://agentskills.io/specification | Портабельный стандарт | Н1 | EN | Free | [`agentskills-specification.md`](./materials-snapshots/agentskills-specification.md) |
| n8n — choose how to use | https://docs.n8n.io/choose-how-to-use-n8n/ | Cloud vs self-host | Н0 | EN | Free | [`n8n-choose-how-to-use.md`](./materials-snapshots/n8n-choose-how-to-use.md) |
| n8n Docker install | https://docs.n8n.io/hosting/installation/docker/ | Local setup | Н0 | EN | Free | [`n8n-docker-install-extracted.md`](./materials-snapshots/n8n-docker-install-extracted.md) |
| n8n AI intro tutorial | https://docs.n8n.io/advanced-ai/intro-tutorial/ | Agent node + chat model + memory | Н1 | EN | Free | Link (HTML; md extract noisy) |
| n8n Webhook node | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/ | Триггер flow #1 | Н1 | EN | Free | [`n8n-webhook-node.md`](./materials-snapshots/n8n-webhook-node.md) |
| n8n Read/Write Files | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/ | Артефакт на диск | Н1 | EN | Free | [`n8n-readwritefile-node.md`](./materials-snapshots/n8n-readwritefile-node.md) |
| n8n blog — AI agents | https://blog.n8n.io/ai-agents/ | Обзор агентов в n8n | Н1 | EN | Free | [`n8n-blog-ai-agents-excerpt.md`](./materials-snapshots/n8n-blog-ai-agents-excerpt.md) |

---

## LinkedIn (courses / creators)

| Title | URL | Why useful | Module | Lang | Free/Paid | Downloadable |
|---|---|---|---|---|---|---|---|
| AI Agents for Product Leaders — Marily Nika | https://www.linkedin.com/learning/ai-agents-for-product-leaders | Короткий foundation agentic products | Н0, Н4 | EN | Paid | No |
| The AI-Native Product Manager’s Toolkit — Marily Nika | https://www.linkedin.com/learning/generative-ai-for-product-managers | AI в цикле PM + verify outputs | Н0, Н3, Н6 | EN | Paid | No |
| Marily Nika (creator) | https://www.linkedin.com/in/marilynika/ | Автор курсов LI Learning / Maven | — | EN | — | — |
| Paweł Huryn / Product Compass | https://www.productcompass.pm/p/pm-skills-2-red-team-ship | Анонс pm-skills 2.0 + red-team | Н1, Н3 | EN | Free article / paid newsletter deeper | Partial |
| Lenny Rachitsky — AI & PM (Marily) | https://www.lennysnewsletter.com/p/ai-and-product-management-marily | Подкаст-рамка «каждый PM = AI PM» | Н0 | EN | Paywall (full) | No |
| Make PM fun again with AI agents (Lenny) | https://www.lennysnewsletter.com/p/make-product-management-fun-again-9f6 | Чеклист безопасного агента | Н1 | EN | Likely paywall | No |

Публичные посты LinkedIn feed в этой среде **не индексируются стабильно** (login wall) — опираемся на Learning + известные creators.

---

## GitHub / papers / tools (флагман)

| Title | URL | Why useful | Module | Lang | Free/Paid | Downloadable |
|---|---|---|---|---|---|---|---|
| AgentA/B paper | https://arxiv.org/abs/2504.09723 | Претест гипотез LLM-агентами | SUL | EN | Free | [`materials-snapshots/agent-ab-arxiv.pdf`](./materials-snapshots/agent-ab-arxiv.pdf) |
| SSR purchase intent | https://arxiv.org/abs/2510.08338 | Методика market eval | Н4, SUL | EN | Free | [`ssr-purchase-intent-arxiv.pdf`](./materials-snapshots/ssr-purchase-intent-arxiv.pdf) |
| SimAB | https://arxiv.org/abs/2603.01024 | Симуляция A/B + accuracy study | SUL | EN | Free | [`simab-arxiv.pdf`](./materials-snapshots/simab-arxiv.pdf) |
| voice-of-agents | https://github.com/blakeaber/voice-of-agents | Pipeline + eval harness | SUL | EN | Free | [`voice-of-agents-README.md`](./materials-snapshots/voice-of-agents-README.md) |
| synthetic-market-research | https://github.com/BayramAnnakov/synthetic-market-research | Skill для synthetic surveys | Н4, SUL | EN | Free | [`synthetic-market-research-README.md`](./materials-snapshots/synthetic-market-research-README.md) |
| semantic-similarity-rating | https://github.com/pymc-labs/semantic-similarity-rating | SSR lib | SUL S3 | EN | Free | [`semantic-similarity-rating-README.md`](./materials-snapshots/semantic-similarity-rating-README.md) |
| phuryn/pm-skills | https://github.com/phuryn/pm-skills | Skills marketplace | Н1–Н7 | EN | Free | [`pm-skills-README.md`](./materials-snapshots/pm-skills-README.md) |
| deanpeters/Product-Manager-Skills | https://github.com/deanpeters/Product-Manager-Skills | PM skills для Claude Code / Codex / Desktop | Н1–Н5 | EN | Free | [`deanpeters-pm-skills-README.md`](./materials-snapshots/deanpeters-pm-skills-README.md) |
| satyapavan1/ai-pm-os | https://github.com/satyapavan1/ai-pm-os | Компактный Claude Code OS для PM (14 skills) | Н1, Н7 | EN | Free | Link only |
| n8n-io/skills (agents TOOLS) | https://github.com/n8n-io/skills | Офиц. reference tool-design для AI Agent node | Н1 | EN | Free | [`n8n-agents-tools-ref.md`](./materials-snapshots/n8n-agents-tools-ref.md) |
| MCP intro | https://modelcontextprotocol.io/docs/getting-started/intro | Внешние инструменты агента | Н1 | EN | Free | [`mcp-intro-extracted.md`](./materials-snapshots/mcp-intro-extracted.md) |
| Synthetic Users (SaaS) | https://www.syntheticusers.com/ | Коммерческий бенчмарк «как делают» | SUL (сравнение) | EN | Freemium/Paid | Landing only |

---

## RU-курсы (конкурентный / партнёрский ландшафт)

| Title | URL | Why useful | Module | Lang | Free/Paid | Downloadable |
|---|---|---|---|---|---|---|---|
| ЯП «Нейросети для продакт-менеджера» | https://practicum.yandex.ru/ai-tools-for-pdm/ | Ближайший RU-конкурент; агенты в расширенных тарифах | сравнение позиционирования | RU | Paid | No |
| ЯП «ИИ-агенты и автоматизация» (n8n) | https://practicum.yandex.com/ai-agents/ | No-code агенты — отличие от нашего harness-трека | Н1 (анти-скоуп glue) | RU | Paid | No |
| Нетология «Управление ИИ-продуктами» | https://netology.ru/programs/ai-product-basic | AI Product Manager как профессия (ML/RAG/ROI) | Н4 (ставка AI в продукте) | RU | Paid | No |
| MLinside AI-агенты для продактов | https://ai4products.mlinside.ru | Backbone программы | все | RU | Paid | No |
| Great Learning — AI for PM (free) | https://www.mygreatlearning.com/academy/learn-for-free/courses/ai-for-product-management | Бесплатный intro EN | Н0 | EN | Free (+paid cert) | No |
| Maven: Agentic AI for PMs | https://maven.com/boring-bot/ml-system-design | Claude Code, evals, orchestration — peer curriculum | Н1, Н4 | EN | Paid | No |

---

## Заблокировано / не сохранено

| Источник | Почему |
|---|---|
| YouTube query `ai для продакта` | SSR/API вернул 0 hits из этой среды; EN-запросы работают |
| LinkedIn feed / posts | Требует логин; доступны только Learning landing pages |
| Lenny Newsletter full text | Paywall |
| Medium full offline | Metered / JS-heavy — стабильного дампа нет |
| Пиратские Mail.ru из kickoff | Намеренно не трогаем |
| DRM / LI Learning video | Не скачиваем |

---

## Как использовать в производстве

1. **Неделя 0–1:** офиц. docs Cursor/Claude/n8n (снапшоты выше) + pm-skills / deanpeters выборочно + Claude-for-PMs YouTube.  
2. **SUL scaffold:** уже в [`course/sul/`](./course/sul/); ethics notice + AgentA/B PDF + (позже) synthetic-market-research skill для S3.  
3. **Не копировать** тексты Medium/Lenny студентам as-is — пересказ + ссылка.  
4. **Не рекомендовать** пиратские дампы; RU-Практикум/Нетология — только как карта рынка.  
5. Карта «неделя → материалы + gaps»: [`course/materials-by-module.md`](./course/materials-by-module.md).
