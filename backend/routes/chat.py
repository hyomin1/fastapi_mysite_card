from fastapi import APIRouter
from backend.services.service_chat import ChatService

router = APIRouter(
    tags=["Chat"], # swagger docs에 나오는 이름
)

# http://127.0.0.1:8000/chat/
@router.post("/")
async def send_message(chat:dict) -> dict:
    print("전달 받은 챗: ",chat)
    answer = ChatService().send_chat(chat)
    return {"answer": answer}