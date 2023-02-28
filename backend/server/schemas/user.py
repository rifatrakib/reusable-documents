from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr, Field


class UserResponse(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    username: str
    email: EmailStr
