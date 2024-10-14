from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from services.transcription import url_checking, transcript
from services.sum import model_summarization, model_summarization_openai, analyze_sentiment, detect_topics
from services.twilio import whatsapp_message, format_summary_message

# Konfiguracja Jinja2
templates = Jinja2Templates(directory="templates")

class YTRequest(BaseModel):
    url: str
    phone_num: str
    model: str

router_youtube = APIRouter(prefix="/yt_transcript")

@router_youtube.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    # Zwracamy template z formularzem
    return templates.TemplateResponse("yt_transcript.html", {"request": request})

@router_youtube.post("/")
async def get_yt_transcript(data: YTRequest):
    video_id = url_checking(data.url)
    transcription = transcript(video_id)
    
    # Wybór modelu na podstawie danych od użytkownika
    if data.model == "openai":
        summary = model_summarization_openai(transcription)
    elif data.model == "custom":
        summary = model_summarization(transcription)
    else:
        return {"status": "error", "message": "Invalid model selected"}


    # Detekcja tematów
    topics = detect_topics(transcription)
    sentiment = analyze_sentiment(transcription)

    formatted_summary = format_summary_message(summary, data.url, topics, sentiment)
    message = whatsapp_message(formatted_summary, data.phone_num)

    
    
    return {"status": "success", "message": message}