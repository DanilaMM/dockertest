import datetime
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class User(BaseModel):
    fullName: str


class ReviewsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True)
    name: str
    userId: str
    raiting: float = Field(ge=0, le=5)
    text: str
    createdAt: str
    user: User
