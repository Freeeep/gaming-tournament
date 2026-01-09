from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.utils.deps import get_current_user
from app.models.user import User
from app.models.tournament import Tournament
from app.models.participant import Participant
from app.models.match import Match
from app.schemas.match import MatchResponse
from app.schemas.tournament import (
    TournamentCreate,
    TournamentResponse,
    TournamentStatus,
    TournamentUpdate,
)
from app.schemas.participant import ParticipantResponse


router = APIRouter(prefix="/tournaments", tags=["Tournaments"])


# Post tournament (create)
@router.post(
    "/", response_model=TournamentResponse, status_code=status.HTTP_201_CREATED
)
def create_tournament(
    tournament_data: TournamentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Create a new tournament.

    The authenticated user becomes the tournament organizer.
    Requires authentication.
    """
    new_tournament = Tournament(
        name=tournament_data.name,
        description=tournament_data.description,
        game=tournament_data.game,
        format=tournament_data.format,
        max_participants=tournament_data.max_participants,
        registration_deadline=tournament_data.registration_deadline,
        start_date=tournament_data.start_date,
        organizer_id=current_user.id,
    )

    db.add(new_tournament)
    db.commit()
    db.refresh(new_tournament)

    return new_tournament


# Get tournaments (list all tournaments)
@router.get("/", response_model=List[TournamentResponse])
def get_tournaments(db: Session = Depends(get_db)):
    """
    Get a list of all tournaments.

    No authentication required.
    """
    tournaments = db.query(Tournament).all()

    return tournaments


# Get tournament {id} details
@router.get("/{tournament_id}", response_model=TournamentResponse)
def get_tournament_id(tournament_id: int, db: Session = Depends(get_db)):
    """
    Get details of a specific tournament by ID.

    No authentication required.
    """
    db_tournament = db.query(Tournament).filter(Tournament.id == tournament_id).first()

    if db_tournament is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )

    return db_tournament


# Put tournament {id} update tournament (organizer only)
@router.put("/{tournament_id}", response_model=TournamentResponse)
def update_tournament(
    tournament_update: TournamentUpdate,
    tournament_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Update a tournament's details.

    Only the tournament organizer can update. Requires authentication.
    Only provided fields will be updated.
    """
    current_tournament = (
        db.query(Tournament).filter(Tournament.id == tournament_id).first()
    )

    if current_tournament is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )

    if current_user.id != current_tournament.organizer_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You are not the organizer"
        )

    update_data = tournament_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(current_tournament, field, value)

    # Save to database
    db.commit()
    db.refresh(current_tournament)

    return current_tournament


# Delete tournament {id} delete tournament (organizer only)
@router.delete("/{tournament_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tournament(
    tournament_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Delete a tournament.

    Only the tournament organizer can delete. Requires authentication.
    This action cannot be undone.
    """
    current_tournament = (
        db.query(Tournament).filter(Tournament.id == tournament_id).first()
    )
    if current_tournament is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )

    if current_user.id != current_tournament.organizer_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You are not the organizer"
        )

    db.delete(current_tournament)
    db.commit()

    return None


# Post tournament {id} join a tournament (get_current_user)
@router.post(
    "/{tournament_id}/join",
    response_model=ParticipantResponse,
    status_code=status.HTTP_201_CREATED,
)
def join_tournament(
    tournament_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Join a tournament as a participant.

    Requires authentication. Users cannot join the same tournament twice.
    """
    tournament = db.query(Tournament).filter(Tournament.id == tournament_id).first()
    if tournament is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found"
        )

    if tournament.status != TournamentStatus.OPEN:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tournament is not open for registration",
        )

    # Check if tournament has full participation

    participant_count = (
        db.query(Participant).filter(Participant.tournament_id == tournament_id).count()
    )

    if participant_count >= tournament.max_participants:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Tournament is full"
        )

    existing = (
        db.query(Participant)
        .filter(
            Participant.tournament_id == tournament_id,
            Participant.user_id == current_user.id,
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already joined this tournament",
        )

    new_participant = Participant(tournament_id=tournament_id, user_id=current_user.id)

    db.add(new_participant)
    db.commit()
    db.refresh(new_participant)

    return new_participant


# Delete tournament {id} leave a tournament (get_current_user)
@router.delete("/{tournament_id}/leave", status_code=status.HTTP_204_NO_CONTENT)
def leave_tournament(
    tournament_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Leave a tournament you have joined.

    Requires authentication. You must be a participant to leave.
    """
    participant = (
        db.query(Participant)
        .filter(
            Participant.tournament_id == tournament_id,
            Participant.user_id == current_user.id,
        )
        .first()
    )

    if participant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="You are not in this tournament",
        )

    db.delete(participant)
    db.commit()

    return None


# Get matches in a tournament
@router.get("/{tournament_id}/matches", response_model=List[MatchResponse])
def get_matches(tournament_id: int, db: Session = Depends(get_db)):
    """
    Get all matches in tournament
    """
    matches = db.query(Match).filter(Match.tournament_id == tournament_id).all()

    return matches


# Get participants in a tournament
@router.get("/{tournament_id}/participants", response_model=List[ParticipantResponse])
def get_participants(tournament_id: int, db: Session = Depends(get_db)):
    """
    Get all participants in tournament
    """
    participants = (
        db.query(Participant).filter(Participant.tournament_id == tournament_id).all()
    )

    return participants
