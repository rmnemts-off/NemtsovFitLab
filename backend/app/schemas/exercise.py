from pydantic import BaseModel, ConfigDict


class MuscleGroupSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class ExerciseShortSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    muscle_group_id: int
    muscle_group: MuscleGroupSchema


class ExerciseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None
    video_file_id: str | None
    muscle_group: MuscleGroupSchema
