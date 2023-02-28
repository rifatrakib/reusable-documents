from importlib import import_module
from typing import List

from beanie import init_beanie
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, parse_obj_as, validator


class MapperSchema(BaseModel):
    name: str
    collections: List[str]

    @validator("collections")
    def validate_class_path(cls, value):
        for path in value:
            try:
                module_name, class_name = path.rsplit(".", 1)
                module = import_module(module_name)
                _ = getattr(module, class_name)
            except (ValueError, ImportError, AttributeError):
                raise ValueError(f"Invalid class path: {path}")
        return value


def database_collection_mapper():
    models = [
        {
            "name": "validation",
            "collections": [
                "documents.user.User",
                "documents.user.Profile",
            ],
        },
    ]

    return parse_obj_as(type_=List[MapperSchema], obj=models)


async def create_database_clients():
    client = AsyncIOMotorClient(settings.MONGO_URI)
    mapper = database_collection_mapper()
    for database in mapper:
        await init_beanie(
            database=client[database.name],
            document_models=database.collections,
        )
