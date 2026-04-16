# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**FitLab** — Telegram Mini App для онлайн-тренера. Клиенты оформляют подписку на программу тренировок, получают тренировки по расписанию и используют библиотеку упражнений. Тренер создаёт тренировки, прикрепляет видео и записывает аудио-брифинг к каждой тренировке.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend (Mini App) | React + TypeScript + Vite |
| Telegram UI Kit | `@telegram-apps/sdk-react` |
| Backend API | Python + FastAPI |
| Telegram Bot | aiogram 3.x |
| Database | PostgreSQL + SQLAlchemy 2.x (async) |
| Migrations | Alembic |
| Media Storage | Telegram file_id (videos/audio) + local `/videos` for seeding |
| Payments | lava.top API (pending integration) |
| Task Queue | Celery + Redis (scheduled workout delivery) |

---

## Repository Structure

```
/
├── backend/          # FastAPI app + aiogram bot
│   ├── app/
│   │   ├── api/      # REST endpoints (for Mini App)
│   │   ├── bot/      # aiogram handlers and middlewares
│   │   ├── models/   # SQLAlchemy ORM models
│   │   ├── schemas/  # Pydantic schemas
│   │   ├── services/ # Business logic
│   │   └── core/     # Config, DB session, auth
│   ├── alembic/      # DB migrations
│   └── main.py       # FastAPI + bot entrypoint
├── frontend/         # React Mini App
│   ├── src/
│   │   ├── pages/    # Route-level components
│   │   ├── components/
│   │   ├── api/      # API client (axios/fetch wrappers)
│   │   └── store/    # Global state (zustand)
│   └── vite.config.ts
├── videos/           # Source exercise videos (used for seeding)
└── docker-compose.yml
```

---

## Core Domain Models

```
User (telegram_id, role: client|trainer)
  └── Subscription (program_id, start_date, end_date, status)

Program (name, description, trainer_id)
  └── Workout (day_number, title, audio_briefing_file_id)
        └── WorkoutExercise (order, sets, reps, notes)
              └── Exercise (name, description, video_file_id, muscle_group_id)

MuscleGroup (name)
  └── Exercise[]
```

Key rules:
- `trainer_id` on Program links to the trainer's `User` record
- `day_number` on Workout is 1-based (Day 1, Day 2…); clients see the workout for their current subscription day
- `video_file_id` and `audio_briefing_file_id` store Telegram `file_id` strings (uploaded via bot)

---

## Key User Flows

### Client
1. Opens Mini App → sees active subscription's today's workout
2. Taps exercise → Exercise Card (video player, name, description, sets/reps)
3. Library tab → MuscleGroups list → Exercises list → Exercise Card
4. Shop tab → available Programs → buy subscription (lava.top / card)

### Trainer (bot commands)
- `/new_workout <program> <day>` — create workout, bot prompts for exercises
- Send video → bot saves `file_id` to Exercise
- Send voice → bot saves `file_id` as workout audio briefing
- `/subscribers` — list active subscriptions per program

---

## Development Commands

### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run dev server (bot + API together)
uvicorn main:app --reload --port 8000

# Migrations
alembic revision --autogenerate -m "description"
alembic upgrade head
```

### Frontend
```bash
cd frontend
npm install
npm run dev       # dev server with hot reload
npm run build     # production build
npm run lint      # eslint
```

### Docker (full stack)
```bash
docker-compose up --build
```

---

## Telegram Mini App Integration

- Mini App is opened via bot's inline keyboard button
- `initData` from `window.Telegram.WebApp` is sent as `Authorization: tma <initData>` header on every API request
- Backend validates `initData` HMAC signature using `BOT_TOKEN` (see `app/core/auth.py`)
- Never trust `telegram_id` from request body — always extract from validated `initData`

---

## Environment Variables

```
BOT_TOKEN=
DATABASE_URL=postgresql+asyncpg://user:pass@localhost/fitlab
REDIS_URL=redis://localhost:6379
LAVA_TOP_API_KEY=
MINI_APP_URL=https://...
```

---

## Conventions

- All API routes are prefixed `/api/v1/`
- Async SQLAlchemy sessions everywhere (`async with async_session() as session`)
- Pydantic v2 schemas; use `model_validate` not `from_orm`
- Exercise videos are uploaded once via bot and referenced by Telegram `file_id` — never store raw video bytes in the DB
