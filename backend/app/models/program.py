from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Program(Base):
    __tablename__ = "programs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    trainer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    workouts: Mapped[list["Workout"]] = relationship(
        back_populates="program", order_by="Workout.day_number"
    )
    subscriptions: Mapped[list["Subscription"]] = relationship(back_populates="program")
