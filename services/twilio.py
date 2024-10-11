from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
account_sid  = os.getenv("TWILIO_SID")
auth_token   = os.getenv("TWILIO_AUTH")
whatsapp_nr   = os.getenv("WHATSAPP_NR")

client = Client(account_sid, auth_token)

def format_summary_message(summary: str, video_url: str) -> str:
    return f"📹 *Video Summary*:\n\n{summary}\n\n🔗 Video URL: {video_url}"


def whatsupp_message(summary:str, phone_num:str):

    message = client.messages.create(
        to=f"whatsapp:{phone_num}",
        from_=f"whatsapp:{whatsapp_nr}",
        body=summary
    )
    return(message.sid)