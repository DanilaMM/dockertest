from pydantic import BaseModel, ConfigDict

class LoginUserDto(BaseModel):
    model_config = ConfigDict(extra="forbid")

    email: str
    password : str