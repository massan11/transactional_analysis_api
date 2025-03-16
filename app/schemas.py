from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    ego_state: str  # Must be "Parent", "Adult", or "Child"

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
