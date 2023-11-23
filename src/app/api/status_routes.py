from fastapi import APIRouter

router = APIRouter()


@router.get("/status_check")
async def status_check():
    """
    API Routing Check
    some async operation could happen here
    example: notes = await get_all_notes()
    """
    return {"verify": "success!"}
