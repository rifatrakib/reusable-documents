from bson.objectid import ObjectId
from server.documents.user import User
from server.schemas.user import UserResponse

from models.user import UserModel


async def read_all_user():
    users = await User.find_all().project(UserResponse).to_list()
    return users


async def read_user_by_id(user_id):
    user = await User.find_one(User.id == ObjectId(user_id)).project(UserResponse)
    return user


async def create_new_user(user: UserModel):
    new_user = User(**user.dict())
    new_user = await new_user.insert()
    return new_user
