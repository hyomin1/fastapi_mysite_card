# DB와 커넥션 풀을 생성

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.common.config import Settings


SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# autocommit, autoflush -> False 사용 권장
# - commit 하면 Rollback 불가능!
# - flush 트랜잭션 관련 기능
def get_db():
    print(SQLALCHEMY_DATABASE_URL)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()