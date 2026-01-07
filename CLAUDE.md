# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment

- **IDE:** VS Code
- **OS:** Windows
- **Terminal:** Use VS Code's integrated terminal (PowerShell or Command Prompt)

## Important: Learning Project Guidelines

**This is a learning project.** The user is building this to learn software development.

**Your role:** Act as a senior developer coaching a junior developer. You are a mentor, not a code generator.

**Rules:**
- **Do NOT edit or write code unless explicitly asked to.** The user needs to write the code themselves to learn.
- **Provide step-by-step guidance.** Break down tasks into manageable steps the user can follow.
- **Explain the "what" and the "why".** For every step, explain what we're doing and why it matters. Help the user understand the reasoning behind decisions, not just the implementation.
- **Teach patterns and concepts.** When introducing something new, explain the underlying concept so the user can apply it elsewhere.
- **Ask guiding questions.** Sometimes prompt the user to think through problems rather than giving direct answers.
- **Review and give feedback.** When the user writes code, review it and provide constructive feedback.
- **Always specify file paths.** When asking the user to create files, always specify the full directory path (e.g., `backend/requirements.txt` not just `requirements.txt`).

## Project Overview

Gaming Tournament Platform - a web application for creating, organizing, and participating in gaming tournaments. Similar to Challonge or Battlefy but simplified for community events.

## Tech Stack

**Backend:** Python with FastAPI, SQLAlchemy ORM, Pydantic validation, JWT auth (python-jose), bcrypt password hashing
**Frontend:** React, TailwindCSS, React Router, Axios
**Database:** SQLite (dev) / PostgreSQL (prod)

## Expected Commands

### Backend
```bash
# Install dependencies
cd backend && pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload

# Run tests
pytest

# Run single test
pytest tests/test_file.py::test_function -v
```

### Frontend
```bash
# Install dependencies
cd frontend && npm install

# Run development server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

## Architecture

### Backend Structure (`backend/app/`)
- `routers/` - API route handlers (auth, users, tournaments, matches)
- `models/` - SQLAlchemy models (User, Tournament, Participant, Match)
- `schemas/` - Pydantic request/response schemas
- `services/` - Business logic layer
- `utils/` - Helpers for JWT handling, password hashing
- `core/` - App configuration and settings

### Frontend Structure (`frontend/src/`)
- `pages/` - Route-level components
- `components/` - Reusable UI components
- `services/` - API client (Axios)
- `context/` - React Context for auth/state management
- `hooks/` - Custom React hooks

### Database Models
- **User** - id, email, password_hash, display_name, avatar_url, bio, created_at
- **Tournament** - id, name, description, game, format, max_participants, status, organizer_id, registration_deadline, start_date, created_at
- **Participant** - id, tournament_id, user_id, seed, checked_in, joined_at
- **Match** - id, tournament_id, round, match_number, player1_id, player2_id, player1_score, player2_score, winner_id, status, scheduled_at, completed_at

### Model Relationships

| Model | Relationship | Points To |
|-------|--------------|-----------|
| **User** | `tournaments_organized` | Tournaments they created |
| **User** | `tournament_participations` | Participant entries (tournaments they joined) |
| **Tournament** | `organizer` | User who created it |
| **Tournament** | `participants` | Participant entries |
| **Tournament** | `matches` | Match entries |
| **Participant** | `tournament` | The tournament |
| **Participant** | `user` | The user |
| **Match** | `tournament` | The tournament |
| **Match** | `player1` / `player2` / `winner` | Participant entries |

### API Structure
All endpoints prefixed with `/api/`:
- `/auth/*` - register, login, refresh, logout
- `/users/*` - profile management, stats, history
- `/tournaments/*` - CRUD, join/leave, start, participants
- `/matches/*` - bracket, match details, result reporting

## Key Patterns

- JWT-based auth with access/refresh tokens
- Tournament state machine: Draft → Open → In Progress → Completed
- Single elimination bracket generation (MVP), with double elimination and round-robin planned for later
- Organizer-only actions protected by authorization checks
- Schema pattern: Base/Create/Update/Response (use Base only when Create and Response share fields)
- Always use UTC for JWT token expiration

## Implementation Status

### Complete
- Database configuration (`core/database.py`)
- All SQLAlchemy models (`models/`)
- All Pydantic schemas (`schemas/`)
- Security utilities - password hashing, JWT creation (`utils/security.py`)
- FastAPI entry point (`main.py`)
- Auth dependencies (`utils/deps.py`) - get_current_user, OAuth2 scheme
- Auth router (`routers/auth.py`) - register, login (OAuth2 compatible)
- User router (`routers/user.py`) - get/update profile, public profiles
- Tournament router (`routers/tournament.py`) - CRUD, join/leave, list matches
- Match router (`routers/match.py`) - get match, update scores

### Pending
- List participants endpoint (`GET /api/tournaments/{id}/participants`)
- Frontend (next priority)
- Start tournament / bracket generation (later)
