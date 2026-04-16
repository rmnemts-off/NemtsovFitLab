from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import TelegramUserInfo, get_current_telegram_user_info
from app.core.database import get_session
from app.models.user import User
from app.services import user_service


async def get_current_user(
    user_info: TelegramUserInfo = Depends(get_current_telegram_user_info),
    session: AsyncSession = Depends(get_session),
) -> User:
    return await user_service.get_or_create_user(
        session=session,
        telegram_id=user_info.telegram_id,
        full_name=user_info.full_name,
        username=user_info.username,
    )
