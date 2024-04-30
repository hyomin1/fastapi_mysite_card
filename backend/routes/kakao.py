from fastapi import APIRouter

router = APIRouter(
    tags=["Kakao"],
)

# http://127.0.0.1:8000/kakao/
@router.post("/")
async def send_message(msg:MessageDTO) -> dict:
    return {"status": {"code":200, "message": "success"}}