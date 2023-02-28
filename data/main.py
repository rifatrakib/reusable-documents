import asyncio

from database.manager import create_database_clients
from database.user import upload_profile_data, upload_user_data


async def runner():
    await create_database_clients()
    await upload_user_data()
    await upload_profile_data()


if __name__ == "__main__":
    asyncio.run(runner())
