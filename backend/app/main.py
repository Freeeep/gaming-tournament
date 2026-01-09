from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
from app.routers.auth import router as auth_router
from app.routers.user import router as user_router
from app.routers.tournament import router as tournament_router
from app.routers.match import router as match_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gaming Tournament API",
    description="API for managing gaming tournaments",
    version="0.1.0",
)

# Allow frontend to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://192.168.68.69:5173",
        "http://localhost:5173",
        "http://192.168.68.69:8000/api",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(tournament_router, prefix="/api")
app.include_router(match_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to the Gaming Tournament API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
