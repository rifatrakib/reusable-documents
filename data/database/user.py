from typing import List

from documents.user import Profile, User
from pydantic import parse_file_as


async def upload_user_data():
    user_data = parse_file_as(path="resources/user.json", type_=List[User])
    await User.insert_many(user_data)


async def upload_profile_data():
    profile_data = parse_file_as(path="resources/profile.json", type_=List[Profile])
    await Profile.insert_many(profile_data)
