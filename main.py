# uvicorn main:app --reload    # was 실행

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from backend.routes import kakao, chat
from apscheduler.schedulers.background import BackgroundScheduler
from backend.services.service_kakao import KakaoService
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="static"), name="static") 

app.include_router(kakao.router, prefix="/kakao")
app.include_router(chat.router, prefix="/chat")


@app.get("/")  # http://127.0.0.1:8000/
async def welcome(request: Request) -> dict:
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    sched = BackgroundScheduler()
    sched.add_job(KakaoService().refresh_access_token, "cron", day="1", hour="0", id="refresh_token")  # 매월 1일 refresh_token 재발급
    sched.start()
    
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    


