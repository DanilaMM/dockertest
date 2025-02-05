import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class User(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True,
                              arbitrary_types_allowed=True)

    id: UUID
    email: str
    full_name: str = Field(alias="fullName")
    roles: List[str]
    created_at: datetime = Field(alias="createdAt")
    banned: bool


class LoginResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    user: User
    access_token: str = Field(alias="acessToken")
    expires_in: int = Field(alias="expiresIn")
