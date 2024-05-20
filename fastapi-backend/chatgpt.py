# fastapi-backend/app/chatgpt.py
import openai
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat")
async def chat(request: ChatRequest):
    openai.api_key = config.get('KEY', 'OPENAI_API_KEY')
    try:
        response = openai.Completion.create(
            model='gpt-4o'
            engine="text-davinci-003",
            prompt=request.prompt,
            max_tokens=256
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

