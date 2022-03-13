from app.db import notes, database
from app.api.models import NoteSchema


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)


async def get(ids: int):
    query = notes.select().where(ids == notes.c.ids)
    return await database.fetch_one(query=query)


async def get_all():
    query = notes.select()
    return await database.fetch_all(query=query)


async def put(ids: int, payload: NoteSchema):
    query = (
        notes
        .update()
        .where(ids == notes.c.ids)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.ids)
    )
    return await database.execute(query=query)


async def delete(ids: int):
    query = notes.delete().where(ids == notes.c.ids)
    return await database.execute(query=query)
