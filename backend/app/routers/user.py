from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate, UserPrivateResponse
from app.utils.deps import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserPrivateResponse)
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    """
    Get the currently authenticated user's profile.

    Returns private profile data including email.
    Requires authentication.
    """
    return current_user


@router.put("/me", response_model=UserPrivateResponse)
def update_current_user_profile(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Update the currently authenticated user's profile.

    Only provided fields will be updated. Requires authentication.

    - **display_name**: Optional new display name
    - **avatar_url**: Optional URL to avatar image
    - **bio**: Optional user biography
    """

    # Get only the fields that were actually sent (not None)
    update_data = user_update.model_dump(exclude_unset=True)

    # Loop through and apply each field to the user
    for field, value in update_data.items():
        setattr(current_user, field, value)

    # Save to database
    db.commit()
    db.refresh(current_user)  # Refresh to get any DB-generated values

    return current_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user's public profile by their ID.

    Returns public profile data (no email). No authentication required.
    """
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return db_user
