# Progress Log

## 06/Jan/2026

### Accomplished
- Created project folder structure (backend & frontend directories)
- Set up Python virtual environment and installed dependencies
- Created `backend/requirements.txt` with FastAPI, SQLAlchemy, Pydantic, JWT, bcrypt packages
- Initialized git repo and pushed to GitHub (https://github.com/Freeeep/gaming-tournament)
- Created database configuration (`backend/app/core/database.py`)
- Created all 4 SQLAlchemy models with relationships:
  - `User` - authentication and profile fields
  - `Tournament` - with status/format enums, linked to organizer
  - `Participant` - junction table linking users to tournaments
  - `Match` - with player references and status tracking
- Created FastAPI entry point (`backend/app/main.py`) with database table creation
- Created all Pydantic schemas for request/response validation:
  - `user.py`, `tournament.py`, `participant.py`, `match.py`
- Created `backend/app/utils/security.py` with password hashing and JWT token creation
- Updated `CLAUDE.md` with learning project guidelines, dev environment, and model relationships
- Updated `planning.md` with model relationships summary

### Notes
- This is a learning project - Claude acts as a senior developer coaching, not writing code
- User is developing in VS Code on Windows
- VS Code may show yellow lines for imports if venv interpreter not selected (doesn't affect functionality)
- Using UTC for JWT token expiration (standard practice)
- SECRET_KEY is placeholder - will use environment variables for production

### Tomorrow
- Create `backend/app/utils/deps.py` (auth dependencies for protecting routes)
- Build the auth router (register/login endpoints)
- Test authentication flow
