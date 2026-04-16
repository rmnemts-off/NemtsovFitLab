from datetime import date
from enum import Enum as PyEnum

from sqlalchemy import Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class SubscriptionStatus(str, PyEnum):
    active = "active"
    expired = "expired"
    pending = "pending"  # payment initiated but not confirmed


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    program_id: Mapped[int] = mapped_column(ForeignKey("programs.id"))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    status: Mapped[SubscriptionStatus] = mapped_column(
        Enum(SubscriptionStatus), default=SubscriptionStatus.pending
    )

    user: Mapped["User"] = relationship(back_populates="subscriptions")
    program: Mapped["Program"] = relationship(back_populates="subscriptions")

    @property
    def current_day(self) -> int:
        """Day number in the program (1-based) based on subscription start date."""
        from datetime import date as today_date
        delta = (today_date.today() - self.start_date).days + 1
        return max(1, delta)
