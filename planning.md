# Gaming Tournament Platform

## What Is It?

A web application that allows gamers to create, organize, and participate in gaming tournaments. Users can register accounts, create tournaments for any game, invite players, generate brackets automatically, track match results in real-time, and view standings and statistics. Think of it as your own simplified version of Challonge or Battlefy - a platform where communities can run their own competitive events without needing spreadsheets or manual bracket management.

---

## Similar Products in the Market

### Challonge
- Owned by Logitech, hosted over 31 million brackets
- Known for simple interface and quick setup
- Supports single elimination, double elimination, round-robin
- Real-time bracket updates and social sharing
- **Pricing:** Free basic tier, $12/month premium

### Battlefy
- Operating since 2013, headquartered in Vancouver
- Flexible bracket tools with automated player check-in
- Direct in-game integration for popular esports titles
- Dispute management system
- Supports: Valorant, League of Legends, Apex Legends, Rocket League, etc.
- **Pricing:** Free core features, custom pricing for enterprise

### Toornament
- Used by Riot Games, Ubisoft, Bethesda
- Comprehensive platform with multi-platform support
- Extensive customization and robust API
- Designed for professional esports leagues
- **Pricing:** Free limited tier, $59/month premium

### Key Differentiators of Existing Platforms
| Platform   | Best For                          | Key Strength              |
|------------|-----------------------------------|---------------------------|
| Challonge  | Quick grassroots tournaments      | Ease of use               |
| Battlefy   | Community and enterprise events   | Game integrations         |
| Toornament | Professional esports leagues      | Customization & API       |

---

## Core Features

### Authentication & Users
- User registration with email and password
- JWT-based authentication with access/refresh tokens
- User profiles with display name, avatar, and bio
- User statistics (tournaments played, wins, losses, win rate)

### Tournament Management
- Create tournaments with customizable settings:
  - Tournament name and description
  - Game title
  - Format (single elimination, double elimination, round-robin)
  - Maximum participants
  - Registration deadline
  - Start date/time
- Tournament states: Draft → Open → In Progress → Completed
- Public or private tournaments (invite-only with codes)
- Tournament organizer controls (edit, cancel, manage participants)

### Registration & Participation
- Browse open tournaments with filtering (by game, status, date)
- Join tournaments (with optional check-in requirement)
- Leave tournaments before they start
- View registered participants

### Bracket Generation & Matches
- Automatic bracket generation based on format
- Seeding options (random, manual, by ranking)
- Match scheduling with round progression
- Report match results (scores, winner)an
- Match dispute system (organizer resolves)

### Live Updates & Standings
- Real-time bracket visualization
- Current standings and progression
- Match history for each tournament
- Player progression tracking through rounds

### Statistics & History
- User match history
- Head-to-head records
- Tournament history (participated, organized)
- Leaderboards by game

---

## API Endpoints (Planned)

### Authentication
```
POST   /api/auth/register       - Create new account
POST   /api/auth/login          - Login, receive tokens
POST   /api/auth/refresh        - Refresh access token
POST   /api/auth/logout         - Invalidate tokens
```

### Users
```
GET    /api/users/me            - Get current user profile
PATCH  /api/users/me            - Update current user profile
GET    /api/users/{id}          - Get user by ID
GET    /api/users/{id}/stats    - Get user statistics
GET    /api/users/{id}/tournaments - Get user's tournament history
```

### Tournaments
```
GET    /api/tournaments         - List tournaments (with filters)
POST   /api/tournaments         - Create new tournament
GET    /api/tournaments/{id}    - Get tournament details
PATCH  /api/tournaments/{id}    - Update tournament (organizer only)
DELETE /api/tournaments/{id}    - Cancel tournament (organizer only)
```

### Tournament Participation
```
POST   /api/tournaments/{id}/join    - Join a tournament
DELETE /api/tournaments/{id}/leave   - Leave a tournament
POST   /api/tournaments/{id}/start   - Start the tournament (organizer)
GET    /api/tournaments/{id}/participants - List participants
```

### Brackets & Matches
```
GET    /api/tournaments/{id}/bracket  - Get bracket structure
GET    /api/tournaments/{id}/matches  - List all matches
GET    /api/matches/{id}              - Get match details
PATCH  /api/matches/{id}              - Update match (report results)
```

---

## Tech Stack

### Frontend
- **React** - Component-based UI
- **TailwindCSS** - Styling and responsive design
- **React Router** - Client-side routing
- **Axios** - API communication
- **React Query** (optional) - Data fetching and caching

### Backend
- **Python** - Primary language
- **FastAPI** - Web framework with automatic OpenAPI docs
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Request/response validation
- **python-jose** - JWT token handling
- **passlib** - Password hashing (bcrypt)
- **SQLite** (dev) / **PostgreSQL** (prod) - Database

---

## Database Models (Initial Design)

### User
- id, email, password_hash, display_name, avatar_url, created_at

### Tournament
- id, name, description, game, format, max_participants
- status (draft, open, in_progress, completed, cancelled)
- organizer_id (FK to User)
- registration_deadline, start_date, created_at

### Participant
- id, tournament_id, user_id, seed, checked_in, joined_at

### Match
- id, tournament_id, round, match_number
- player1_id, player2_id (FK to Participant)
- player1_score, player2_score, winner_id
- status (pending, in_progress, completed)
- scheduled_at, completed_at

### Model Relationships Summary

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

---

## Learning Goals

By building this project, you will learn:

1. **API Design** - RESTful endpoint structure, resource modeling, HTTP methods
2. **Authentication** - JWT tokens, password hashing, protected routes
3. **Authorization** - Role-based access (organizer vs participant vs viewer)
4. **State Management** - Tournament lifecycle, match progression
5. **Database Relationships** - One-to-many, many-to-many with SQLAlchemy
6. **Validation** - Pydantic models for request/response validation
7. **Error Handling** - Consistent error responses, HTTP status codes
8. **Pagination & Filtering** - Query parameters for list endpoints
9. **Frontend-Backend Integration** - React consuming your own API

---

## MVP Scope (Phase 1)

For the initial version, focus on:

1. User registration and login (JWT auth)
2. Create and list tournaments
3. Join/leave tournaments
4. Start tournament and generate single-elimination bracket
5. Report match results
6. View bracket and standings
7. Basic tournament filtering

Save for later:
- Double elimination / round-robin formats
- Check-in system
- Match disputes
- Real-time websocket updates
- User avatars and advanced profiles

---

## Sources

- [Battlefy - Esports Tournament Platform](https://battlefy.com/)
- [Challonge - Tournament Brackets](https://challonge.com/)
- [Toornament - Esports Management](https://www.toornament.com/)
- [15 Best Tournament Tools in 2025](https://mycup.me/blog/best-tournament-software/)
- [Battlefy Review - Nerdisa](https://nerdisa.com/battlefy/)
