# DAO(Data Access Object)
from backend.schemas.message import MessageDTO
from backend.models.message import MessageORM
from datetime import datetime
from sqlalchemy.orm import Session
# Schemas-MessageDTO: 데이터 전달, 유효성 체크
# Models-MessageORM: ORM을 활용하기 위한 객체화
def create_message(msg:MessageDTO, db: Session):
    # 객체생성 -> 생성자함수(ex: 객체이름())
    db_msg = MessageORM(
        name=msg.name,
        email=msg.email,
        message=msg.message,
        create_date=datetime.now()
    )
    # db_msg -> 인스턴스(객체 생성의 결과물)
    # db -> Connection 된 session!
    db.add(db_msg)
    db.commit()

