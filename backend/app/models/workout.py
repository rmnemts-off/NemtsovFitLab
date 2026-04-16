from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Workout(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(primary_key=True)
    program_id: Mapped[int] = mapped_column(ForeignKey("programs.id"))
    day_number: Mapped[int] = mapped_column(Integer)  # 1-based
    title: Mapped[str] = mapped_column(String(255))
    audio_briefing_file_id: Mapped[str | None] = mapped_column(String(255), nullable=True)

    program: Mapped["Program"] = relationship(back_populates="workouts")
    exercises: Mapped[list["WorkoutExercise"]] = relationship(
        back_populates="workout", order_by="WorkoutExercise.order"
    )
