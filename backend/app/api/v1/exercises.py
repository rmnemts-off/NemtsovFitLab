from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_session
from app.models.user import User
from app.schemas.exercise import ExerciseSchema, ExerciseShortSchema, MuscleGroupSchema
from app.services import exercise_service

router = APIRouter()


@router.get("/muscle-groups", response_model=list[MuscleGroupSchema])
async def get_muscle_groups(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """Return all muscle groups."""
    return await exercise_service.get_muscle_groups(session)


@router.get("/muscle-groups/{group_id}", response_model=list[ExerciseShortSchema])
async def get_exercises_by_group(
    group_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """Return all exercises for a muscle group."""
    return await exercise_service.get_exercises_by_group(session, group_id)


@router.get("/{exercise_id}", response_model=ExerciseSchema)
async def get_exercise(
    exercise_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """Return a single exercise card."""
    exercise = await exercise_service.get_exercise(session, exercise_id)
    if exercise is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercise not found.",
        )
    return exercise
