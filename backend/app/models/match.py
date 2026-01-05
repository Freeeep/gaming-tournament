from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum


from app.core.database import Base

class MatchStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    round = Column(Integer, nullable=False)
    match_number = Column(Integer, nullable=False)
    player1_id = Column(Integer, ForeignKey("participants.id"), nullable=True)
    player2_id = Column(Integer, ForeignKey("participants.id"), nullable=True)
    player1_score = Column(Integer, nullable=True)
    player2_score = Column(Integer, nullable=True)
    winner_id = Column(Integer, ForeignKey("participants.id"), nullable=True)
    status = Column(Enum(MatchStatus), default=MatchStatus.PENDING)
    scheduled_at = Column(DateTime(timezone=True), nullable=False)
    completed_at = Column(DateTime(timezone=True))

    # Relationships
    tournament = relationship("Tournament", back_populates="matches")
    player1 = relationship("Participant", foreign_keys=[player1_id])
    player2 = relationship("Participant", foreign_keys=[player2_id])
    winner = relationship("Participant", foreign_keys=[winner_id])

