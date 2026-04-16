from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_session
from app.models.subscription import Subscription, SubscriptionStatus
from app.models.user import User
from app.schemas.subscription import SubscriptionSchema

router = APIRouter()


@router.get("/my", response_model=list[SubscriptionSchema])
async def get_my_subscriptions(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """Return active subscriptions for the current user."""
    today = date.today()
    result = await session.execute(
        select(Subscription).where(
            Subscription.user_id == current_user.id,
            Subscription.status == SubscriptionStatus.active,
            Subscription.end_date >= today,
        )
    )
    subscriptions = result.scalars().all()
    return [SubscriptionSchema.model_validate(s) for s in subscriptions]


@router.post("/")
async def create_subscription(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """Initiate subscription purchase (lava.top or manual)."""
    pass
