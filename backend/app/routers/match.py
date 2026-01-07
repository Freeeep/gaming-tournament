from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.utils.deps import get_current_user
from app.models.user import User
from app.models.match import Match
from app.models.tournament import Tournament
from app.schemas.match import MatchResponse, MatchUpdate

router = APIRouter(
    prefix="/matches",
    tags=["Matches"]
)

@router.get("/{match_id}", response_model=MatchResponse)
def get_match(match_id: int,
              db: Session = Depends(get_db)):
    
    """
    Get match details of a specific match by ID

    Does not require authentication
    """

    db_match = db.query(Match).filter(Match.id == match_id).first()

    if db_match is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found"
        )
    
    return db_match

@router.put("/{match_id}", response_model=MatchResponse)
def update_match(match_id: int,
                 match_update: MatchUpdate,
                 current_user: User = Depends(get_current_user),
                 db: Session = Depends(get_db)):
    
    """
    Update match details of a specific match ID

    Require authentication
    """
    
    match = db.query(Match).filter(Match.id == match_id).first()

    if match is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found"
        )
    
    tournament = db.query(Tournament).filter(Tournament.id == match.tournament_id).first()
    if current_user.id != tournament.organizer_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not the organizer"
        )

    
    update_data = match_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(match, field, value)

    db.commit()
    db.refresh(match)

    return match

    

