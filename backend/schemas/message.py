from pydantic import BaseModel, Field, EmailStr

#Pydantic : 유효성 체크
class MessageDTO(BaseModel):
    name: str
    email: EmailStr = Field(default=None, title="기본 이메일 형식")
    message: str
