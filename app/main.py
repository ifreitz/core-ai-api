from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat_ai

app = FastAPI()
app.include_router(chat_ai.router, prefix="/chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}
