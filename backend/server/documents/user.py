from beanie import Document

from models.user import ProfileModel, UserModel


class User(Document, UserModel):
    class Settings:
        name = "users"
        indexes = ["username", "email"]


class Profile(Document, ProfileModel):
    class Settings:
        name = "profiles"
        indexes = ["user.username", "user.email"]
