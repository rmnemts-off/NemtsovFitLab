from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import get_current_telegram_id
from app.core.database import get_session

router = APIRouter()


@router.get("/muscle-groups")
async def get_muscle_groups(
    telegram_id: int = Depends(get_current_telegram_id),
    session: AsyncSession = Depends(get_session),
):
    """Return all muscle groups."""
    # TODO: implement via ExerciseService
    pass


@router.get("/muscle-groups/{group_id}")
async def get_exercises_by_group(
    group_id: int,
    telegram_id: int = Depends(get_current_telegram_id),
    session: AsyncSession = Depends(get_session),
):
    """Return all exercises for a muscle group."""
    pass


@router.get("/{exercise_id}")
async def get_exercise(
    exercise_id: int,
    telegram_id: int = Depends(get_current_telegram_id),
    session: AsyncSession = Depends(get_session),
):
    """Return a single exercise card."""
    pass
