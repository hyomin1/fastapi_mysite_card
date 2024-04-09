# uvicorn main:app --reload   # was 실행

import uvicorn 
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
app.mount("/static",StaticFiles(directory="static"), name="static")


@app.get("/") # http://127.0.0.1:8000/
async def welcome(request:Request):
    return templates.TemplateResponse("index.html",{"request": request})