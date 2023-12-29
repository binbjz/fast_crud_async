from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import notes, status_routes
from app.db import database, engine, metadata

metadata.create_all(engine)


@asynccontextmanager
async def app_lifespan(app_instance: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=app_lifespan)

app.include_router(status_routes.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])


@app.get("/predict")
async def predict(x: float):
    return {"result": "predict result"}

