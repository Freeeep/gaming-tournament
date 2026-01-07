from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.models.match import MatchStatus

class MatchUpdate(BaseModel):
    status: Optional[MatchStatus] = None
    scheduled_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    player1_score: Optional[int] = None
    player2_score: Optional[int] = None
    player1_id: Optional[int] = None
    player2_id: Optional[int] = None
    winner_id: Optional[int] = None

class MatchResponse(BaseModel):
    id: int
    tournament_id: int
    match_number: int
    round: int
    player1_id: Optional[int] = None
    player2_id: Optional[int] = None
    player1_score: Optional[int] = None
    player2_score: Optional[int] = None
    winner_id: Optional[int] = None
    status: MatchStatus
    scheduled_at: datetime
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True