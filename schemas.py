from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(UserCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
