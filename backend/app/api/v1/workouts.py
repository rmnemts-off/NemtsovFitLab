from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_session
from app.models.user import User
from app.schemas.workout import WorkoutSchema
from app.services import workout_service

router = APIRouter()


@router.get("/today", response_model=WorkoutSchema)
async def get_today_workout(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """Return the current day's workout for the authenticated client."""
    workout = await workout_service.get_today_workout(session, current_user.telegram_id)
    if workout is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active subscription or no workout for today.",
        )
    return workout


@router.get("/{workout_id}", response_model=WorkoutSchema)
async def get_workout_by_id(
    workout_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """Return a specific workout by ID."""
    workout = await workout_service.get_workout_by_id(session, workout_id)
    if workout is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workout not found.",
        )
    return workout
