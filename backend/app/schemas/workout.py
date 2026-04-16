from pydantic import BaseModel, ConfigDict

from app.schemas.exercise import ExerciseShortSchema


class WorkoutExerciseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order: int
    sets: int | None
    reps: str | None
    notes: str | None
    exercise: ExerciseShortSchema


class WorkoutSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    day_number: int
    title: str
    audio_briefing_file_id: str | None
    exercises: list[WorkoutExerciseSchema]
