from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.subscription import Subscription, SubscriptionStatus
from app.models.user import User
from app.models.workout import Workout
from app.schemas.workout import WorkoutSchema


def _workout_load_options():
    """selectinload chain: WorkoutExercise → Exercise → MuscleGroup."""
    from app.models.workout_exercise import WorkoutExercise
    from app.models.exercise import Exercise

    return [
        selectinload(Workout.exercises).selectinload(WorkoutExercise.exercise).selectinload(
            Exercise.muscle_group
        )
    ]


async def get_today_workout(session: AsyncSession, telegram_id: int) -> WorkoutSchema | None:
    # 1. Resolve user
    user_result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
    )
    user = user_result.scalar_one_or_none()
    if user is None:
        return None

    # 2. Find active subscription
    today = date.today()
    sub_result = await session.execute(
        select(Subscription).where(
            Subscription.user_id == user.id,
            Subscription.status == SubscriptionStatus.active,
            Subscription.end_date >= today,
        )
    )
    subscription = sub_result.scalar_one_or_none()
    if subscription is None:
        return None

    current_day = subscription.current_day

    # 3. Find workout for that day_number in the program
    workout_result = await session.execute(
        select(Workout)
        .where(
            Workout.program_id == subscription.program_id,
            Workout.day_number == current_day,
        )
        .options(*_workout_load_options())
    )
    workout = workout_result.scalar_one_or_none()
    if workout is None:
        return None

    return WorkoutSchema.model_validate(workout)


async def get_workout_by_id(session: AsyncSession, workout_id: int) -> WorkoutSchema | None:
    result = await session.execute(
        select(Workout)
        .where(Workout.id == workout_id)
        .options(*_workout_load_options())
    )
    workout = result.scalar_one_or_none()
    if workout is None:
        return None
    return WorkoutSchema.model_validate(workout)
