from pydantic import BaseModel

#Pydantic : 유효성 체크
class MessageDTO(BaseModel):
    name: str
    email: str
    message: str
