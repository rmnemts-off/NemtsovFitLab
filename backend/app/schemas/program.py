from pydantic import BaseModel, ConfigDict


class ProgramSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None
