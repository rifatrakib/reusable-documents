from fastapi import FastAPI
from server.database.factory import create_database_clients
from server.routes.user import router as user_router

app = FastAPI()
app.include_router(user_router)


@app.on_event("startup")
async def startup():
    await create_database_clients()
