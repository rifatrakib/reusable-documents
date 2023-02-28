from typing import List

from fastapi import APIRouter, Path
from server.database.user import create_new_user, read_all_user, read_user_by_id
from server.schemas.user import UserResponse

from models.user import UserModel

router = APIRouter(prefix="/users")


@router.get("", response_model=List[UserResponse])
async def read_users():
    return await read_all_user()


@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: str = Path()):
    return await read_user_by_id(user_id)


@router.post("", response_model=UserResponse)
async def create_user(user: UserModel):
    return await create_new_user(user)
