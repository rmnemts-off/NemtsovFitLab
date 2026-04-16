from fastapi import APIRouter

from app.api.v1 import workouts, exercises, subscriptions, programs

api_router = APIRouter()

api_router.include_router(workouts.router, prefix="/workouts", tags=["workouts"])
api_router.include_router(exercises.router, prefix="/exercises", tags=["exercises"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
api_router.include_router(programs.router, prefix="/programs", tags=["programs"])
