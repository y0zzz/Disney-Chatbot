"""FastAPI entrypoint for the Disney chatbot."""
 
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
 
from app.disneychatbot import DisneyChatbot
 
logging.basicConfig(level=logging.INFO)
 
app = FastAPI(
    title="Disney Chatbot",
    description="A small Q&A chatbot for Disney movie and company trivia.",
    version="2.1.0",
)
 
# Allow the static frontend (served from a different origin) to call this API.
# Tighten allow_origins to your actual deployed frontend URL before going to production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
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
async def chat(payload: ChatRequest) -> ChatResponse:
    reply = await chatbot.respond(payload.message)
    return ChatResponse(response=reply)
 
 
if __name__ == "__main__":
    import uvicorn
 
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
 