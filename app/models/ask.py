from pydantic import BaseModel


class Ask(BaseModel):
    history: list[dict]
    message: str
