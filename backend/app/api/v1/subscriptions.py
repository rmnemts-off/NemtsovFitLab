from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import get_current_telegram_id
from app.core.database import get_session

router = APIRouter()


@router.get("/my")
async def get_my_subscriptions(
    telegram_id: int = Depends(get_current_telegram_id),
    session: AsyncSession = Depends(get_session),
):
    """Return active subscriptions for the current user."""
    pass


@router.post("/")
async def create_subscription(
    telegram_id: int = Depends(get_current_telegram_id),
    session: AsyncSession = Depends(get_session),
):
    """Initiate subscription purchase (lava.top or manual)."""
    pass
