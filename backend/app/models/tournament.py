from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.core.database import Base

class TournamentStatus(enum.Enum):
    DRAFT = "draft"
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TournamentFormat(enum.Enum):
    SINGLE_ELIMINATION = "single_elimination"
    DOUBLE_ELIMINATION = "double_elimination"
    ROUND_ROBIN = "round_robin"

class Tournament(Base):
    __tablename__ = "tournaments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    game = Column(String, nullable=False)
    format = Column(Enum(TournamentFormat), default=TournamentFormat.SINGLE_ELIMINATION)
    max_participants = Column(Integer, default=16)
    status = Column(Enum(TournamentStatus), default=TournamentStatus.DRAFT)
    organizer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    registration_deadline = Column(DateTime(timezone=True), nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    #Relationships
    organizer = relationship("User", back_populates="tournaments_organized")
    participants = relationship("Participant", back_populates="tournament")
    matches = relationship("Match", back_populates="tournament")