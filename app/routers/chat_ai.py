from fastapi import APIRouter
from app.config import settings
from google import generativeai as genai

from app.models.ask import Ask

router = APIRouter()

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


@router.post("/ask")
async def ask(payload: Ask):
    """
    Initiates a chat session with the AI model and sends a message.

    Parameters:
    - payload: Ask
        - history: list of dictionaries representing the chat history
            - role: str, either "user" or "model"
            - parts: str, the message part
        - message: str, the message to be sent to the AI model

    Returns:
    - dict with a single key "response" containing the text response from the AI model
    """
    chat = model.start_chat(history=payload.history)
    response = chat.send_message(payload.message)
    return {"response": response.text}
