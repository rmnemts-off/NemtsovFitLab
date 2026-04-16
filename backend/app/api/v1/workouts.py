from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import get_current_telegram_id
from app.core.database import get_session

router = APIRouter()


@router.get("/today")
async def get_today_workout(
    telegram_id: int = Depends(get_current_telegram_id),
    session: AsyncSession = Depends(get_session),
):
    """Return the current day's workout for the authenticated client."""
    # TODO: implement via WorkoutService
    pass
