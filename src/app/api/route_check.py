from fastapi import APIRouter

router = APIRouter()


@router.get("/rt_chk")
async def rt_chk():
    """
    API Routing Check
    some async operation could happen here
    example: notes = await get_all_notes()
    """
    return {"verify": "success!"}
