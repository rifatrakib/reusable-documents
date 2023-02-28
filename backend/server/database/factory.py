from typing import List

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import parse_obj_as
from server.config.factory import settings
from server.schemas.base import MapperSchema


def database_collection_mapper():
    models = [
        {
            "name": "validation",
            "collections": [
                "server.documents.user.User",
                "server.documents.user.Profile",
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
