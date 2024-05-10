# ORM: 테이블 -> 객체화

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MessageORM(Base):
    __tablename__ = "tbl_message" # 실제 테이블 명
    
    no = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

    def __init__(self, name, email, message, create_date):
        self.name = name
        self.email = email
        self.message = message
        self.create_date = create_date

