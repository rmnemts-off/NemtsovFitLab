from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class MuscleGroup(Base):
    __tablename__ = "muscle_groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)

    exercises: Mapped[list["Exercise"]] = relationship(back_populates="muscle_group")


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    video_file_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    muscle_group_id: Mapped[int] = mapped_column(ForeignKey("muscle_groups.id"))

    muscle_group: Mapped["MuscleGroup"] = relationship(back_populates="exercises")
