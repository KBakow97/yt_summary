from fastapi import APIRouter, Request
from services.transcription import url_checking, transcript
from services.sum import model_summarization, model_summarization_openai
from services.twilio import whatsupp_message, format_summary_message
from twilio.twiml.messaging_response import MessagingResponse

router_youtube = APIRouter(
    prefix="/yt_transcript"
)

@router_youtube.post("/")
def get_yt_transcript(url:str,phone_num:str):
    video_id = url_checking(url)
    transcription = transcript(video_id)
    summary = model_summarization_openai(transcription)
    formatted_summary = format_summary_message(summary,url)

    message = whatsupp_message(formatted_summary, phone_num)
    return message

