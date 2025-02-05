from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class CreateReviews(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True)
    rating: str
    text: str
