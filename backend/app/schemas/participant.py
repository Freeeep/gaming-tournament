from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ParticipantUpdate(BaseModel):
    seed: Optional[int] = None
    checked_in: Optional[bool] = None

class ParticipantResponse(BaseModel):
    tournament_id: int
    user_id: int
    id: int
    seed: Optional[int] = None ## Is optional as it may return null as the user has an option to keep empty
    checked_in: bool
    joined_at: datetime

    class Config:
        from_attributes = True

