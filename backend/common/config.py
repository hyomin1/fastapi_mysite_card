import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

class Settings:

    DB_USERNAME : str = os.getenv('MARIADB_USERNAME')
    DB_PASSWORD: str = os.getenv('MARIADB_PASSWORD')
    DB_HOST : str = os.getenv("MARIADB_HOST", "localhost")
    DB_PORT : str = os.getenv("MARIADB_PORT", "3305") # 3306이 default, 설치시 3306 사용중이라 3305로 해놓음
    DB_DATABASE: str = os.getenv("MARIADB_DATABASE")

    DATABASE_URL = f"mariadb+pymysql:/{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"