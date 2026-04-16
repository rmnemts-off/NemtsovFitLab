from datetime import date

from pydantic import BaseModel, ConfigDict

from app.models.subscription import SubscriptionStatus


class SubscriptionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    program_id: int
    start_date: date
    end_date: date
    status: SubscriptionStatus
    current_day: int
