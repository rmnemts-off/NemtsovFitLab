from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.exercise import Exercise, MuscleGroup
from app.schemas.exercise import ExerciseSchema, ExerciseShortSchema, MuscleGroupSchema


async def get_muscle_groups(session: AsyncSession) -> list[MuscleGroupSchema]:
    result = await session.execute(select(MuscleGroup).order_by(MuscleGroup.name))
    groups = result.scalars().all()
    return [MuscleGroupSchema.model_validate(g) for g in groups]


async def get_exercises_by_group(
    session: AsyncSession, group_id: int
) -> list[ExerciseShortSchema]:
    result = await session.execute(
        select(Exercise)
        .where(Exercise.muscle_group_id == group_id)
        .options(selectinload(Exercise.muscle_group))
        .order_by(Exercise.name)
    )
    exercises = result.scalars().all()
    return [ExerciseShortSchema.model_validate(e) for e in exercises]


async def get_exercise(session: AsyncSession, exercise_id: int) -> ExerciseSchema | None:
    result = await session.execute(
        select(Exercise)
        .where(Exercise.id == exercise_id)
        .options(selectinload(Exercise.muscle_group))
    )
    exercise = result.scalar_one_or_none()
    if exercise is None:
        return None
    return ExerciseSchema.model_validate(exercise)
