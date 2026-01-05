from fastapi import FastAPI

from app.core.database import engine, Base
from app.models import User, Tournament, Participant, Match

Base.metadata.create_all(bind = engine)

app = FastAPI(
    title="Gaming Tournament API",
    description="API for managing gaming tournaments",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Gaming Tournament API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}