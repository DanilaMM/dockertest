from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class LocationEnum(str, Enum):
    SPB = "SPB"
    MSK = "MSK"


class CreateMovieDto(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True)
    name: str
    image_url: str = Field(alias="imageUrl", default="https://image.url")
    price: float
    description: str
    location: LocationEnum
    published: bool
    genre_id: int = Field(alias="genreId")