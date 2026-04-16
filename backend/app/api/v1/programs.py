from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import get_current_telegram_id
from app.core.database import get_session

router = APIRouter()


@router.get("/")
async def get_programs(
    telegram_id: int = Depends(get_current_telegram_id),
    session: AsyncSession = Depends(get_session),
):
    """Return all available programs (for the Shop tab)."""
    pass
