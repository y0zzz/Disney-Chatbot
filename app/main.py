"""FastAPI entrypoint for the Disney chatbot."""

import logging

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.disneychatbot import DisneyChatbot

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Disney Chatbot",
    description="A small Q&A chatbot for Disney movie and company trivia.",
    version="2.0.0",
)

chatbot = DisneyChatbot()


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="The user's question")


class ChatResponse(BaseModel):
    response: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    reply = chatbot.respond(payload.message)
    return ChatResponse(response=reply)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
