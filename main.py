# uvicorn main:app --reload   # was 실행

import uvicorn 
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello FastAPI!"
    }