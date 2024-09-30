from fastapi import FastAPI
from app.routers import chat_ai

app = FastAPI()
app.include_router(chat_ai.router, prefix="/chat")


@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}
