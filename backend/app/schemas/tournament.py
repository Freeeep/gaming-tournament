from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.tournament import TournamentFormat, TournamentStatus


class TournamentBase(BaseModel):
    name: str
    description: Optional[str] = None
    game: str
    format: TournamentFormat = TournamentFormat.SINGLE_ELIMINATION
    max_participants: int = 16


class TournamentCreate(TournamentBase):
    registration_deadline: datetime
    start_date: datetime


class TournamentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    game: Optional[str] = None
    format: Optional[TournamentFormat] = None
    max_participants: Optional[int] = None
    status: Optional[TournamentStatus] = None
    registration_deadline: Optional[datetime] = None
    start_date: Optional[datetime] = None


class TournamentResponse(TournamentBase):
    id: int
    status: TournamentStatus
    organizer_id: int
    registration_deadline: datetime
    start_date: datetime
    created_at: datetime

    class Config:
        from_attributes = True
