from fastapi import APIRouter, HTTPException, Path
from app.api import crud
from app.api.models import NoteDB, NoteSchema

router = APIRouter()


@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response_object = {
        "ids": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.get("/{ids}/", response_model=NoteDB)
async def read_note(ids: int = Path(..., gt=0), ):
    note = await crud.get(ids)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/", response_model=list[NoteDB])
async def read_all_notes():
    return await crud.get_all()


@router.put("/{ids}/", response_model=NoteDB)
async def update_note(payload: NoteSchema, ids: int = Path(..., gt=0), ):
    note = await crud.get(ids)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_id = await crud.put(ids, payload)

    response_object = {
        "ids": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.delete("/{ids}/", response_model=NoteDB)
async def delete_note(ids: int = Path(..., gt=0)):
    note = await crud.get(ids)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    await crud.delete(ids)

    return note
