# Progress Log

## 07/Jan/2026

### Accomplished
- Created User router (`backend/app/routers/user.py`) with 3 endpoints:
  - `GET /api/users/me` - get current user's private profile (includes email)
  - `PUT /api/users/me` - update current user's profile
  - `GET /api/users/{id}` - get any user's public profile (no email)
- Created Tournament router (`backend/app/routers/tournament.py`) with 8 endpoints:
  - `POST /api/tournaments` - create tournament (becomes organizer)
  - `GET /api/tournaments` - list all tournaments
  - `GET /api/tournaments/{id}` - get tournament details
  - `PUT /api/tournaments/{id}` - update tournament (organizer only)
  - `DELETE /api/tournaments/{id}` - delete tournament (organizer only)
  - `POST /api/tournaments/{id}/join` - join tournament
  - `DELETE /api/tournaments/{id}/leave` - leave tournament
  - `GET /api/tournaments/{id}/matches` - list matches in tournament
- Created Match router (`backend/app/routers/match.py`) with 2 endpoints:
  - `GET /api/matches/{id}` - get match details
  - `PUT /api/matches/{id}` - update match/report scores (organizer only)
- Updated auth router to use `OAuth2PasswordRequestForm` for Swagger UI compatibility
- Created `UserPrivateResponse` schema to hide email on public profiles
- Added docstrings to all endpoints for Swagger documentation
- Registered all routers in `main.py`

### Notes
- Learned about `Depends()` for dependency injection in FastAPI
- `model_dump(exclude_unset=True)` only returns fields the client actually sent
- `setattr()` allows dynamic field updates without individual if statements
- HTTP 403 FORBIDDEN for authorization failures vs 401 for authentication failures
- Response models control what data is exposed - use different schemas for public/private data

### Tomorrow
- Add endpoint to list all participants in a tournament (`GET /api/tournaments/{id}/participants`)
- Start React frontend setup

---

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
