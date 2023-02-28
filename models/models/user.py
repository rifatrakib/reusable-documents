from datetime import datetime, timedelta
from typing import Union

from pydantic import BaseModel, EmailStr, Field, HttpUrl, validator


class UserModel(BaseModel):
    username: str = Field(
        title="username",
        decription="""
            Unique username containing letters, numbers, and
            any of (., _, -, @) in between 6 to 32 characters.
        """,
        regex=r"^[\w.@_-]{6,32}$",
        min_length=6,
        max_length=32,
    )
    email: EmailStr = Field(
        title="email",
        decription="Unique email that can be used for user account activation.",
    )
    password: str = Field(
        title="password",
        decription="""
            Password containing at least 1 uppercase letter, 1 lowercase letter,
            1 number, 1 character that is neither letter nor number, and
            between 8 to 32 characters.
        """,
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,64}$",
        min_length=8,
        max_length=64,
    )


class ProfileModel(BaseModel):
    user: UserModel = Field(
        title="user",
        description="User who owns this profile",
    )
    first_name: str = Field(
        title="first name",
        decription="First name of the profile owner.",
        regex=r"^[\w\s]{2,32}$",
        min_length=4,
        max_length=64,
    )
    middle_name: Union[str, None] = Field(
        default=None,
        title="middle name",
        decription="Middle name of the profile owner.",
        regex=r"^[\w\s]{1,32}$",
        min_length=4,
        max_length=128,
    )
    last_name: str = Field(
        title="last name",
        decription="Last name of the profile owner.",
        regex=r"^[\w\s]{2,32}$",
        min_length=4,
        max_length=64,
    )
    birthday: Union[datetime, None] = Field(
        default=None,
        title="birthday",
        description="Date of birth of the profile owner",
    )
    website: Union[HttpUrl, None] = Field(
        default=None,
        title="website",
        description="Personal website of the profile owner",
    )

    @validator("birthday")
    def confirm_adult(cls, v):
        if not v:
            return v

        adult_lower_limit = datetime.utcnow() - timedelta(days=365 * 18)
        if v > adult_lower_limit:
            raise ValueError("Not old enough")
        return v
