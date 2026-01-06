# Progress Log

## 06/Jan/2026 (Session 2)

### Accomplished
- Created `backend/app/utils/deps.py` - auth dependencies with `get_current_user` function
  - OAuth2PasswordBearer scheme for extracting JWT from headers
  - Token decoding and validation with error handling
  - Database lookup to return current user
- Created `backend/app/schemas/auth.py` - AuthLogin & AuthResponse schemas
- Created `backend/app/routers/auth.py` - register and login endpoints
  - Register: validates email uniqueness, hashes password, creates user
  - Login: verifies password, returns JWT token
- Updated `backend/app/main.py` - wired up auth router with `/api` prefix
- Fixed typo in `backend/app/schemas/user.py` - `avatur_url` → `avatar_url`
- Fixed bcrypt version compatibility issue - pinned to 4.0.1 in requirements.txt
- Successfully tested registration and login endpoints via curl

### Notes
- Learned JWT auth flow: password check happens at login, token proves identity after
- `jwt.decode()` does the signature comparison internally using SECRET_KEY
- "Bearer" token type tells clients how to send the token in Authorization header
- bcrypt 4.1+ has compatibility issues with passlib - use 4.0.1

### Tomorrow
- Create User router (`GET/PATCH /api/users/me` - view/update profile)
- Create Tournament router (create and list tournaments)
- Test `get_current_user` dependency with a protected route

---

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
