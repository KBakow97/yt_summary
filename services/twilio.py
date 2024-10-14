from twilio.rest import Client
from dotenv import load_dotenv
import time
import os

load_dotenv()
account_sid  = os.getenv("TWILIO_SID")
auth_token   = os.getenv("TWILIO_AUTH")
whatsapp_nr   = os.getenv("WHATSAPP_NR")

client = Client(account_sid, auth_token)

def format_summary_message(summary: str, video_url: str, topic:str, sentiment:str) -> str:
    return f"📹 *Video Summary*:\n\n{summary}\n\n🔗 Video URL: {video_url}\n\n Topic: {topic}\n\n Tone of speech: {sentiment}"


def whatsapp_message(summary: str, phone_num: str):
    # Podziel wiadomość na fragmenty o maksymalnej długości 1400 znaków
    messages = [summary[i:i + 1400] for i in range(0, len(summary), 1400)]
    
    message_sids = []
    for idx, msg in enumerate(messages):
        try:
            message = client.messages.create(
                to=f"whatsapp:{phone_num}",
                from_=f"whatsapp:{whatsapp_nr}",
                body=f"Part {idx + 1}/{len(messages)}: {msg}" if len(messages) > 1 else msg
            )
            message_sids.append(message.sid)  # Zbieraj identyfikatory wiadomości
            time.sleep(2)
        except Exception as e:
            print(f"Error sending message part {idx + 1}: {e}")
    
    return message_sids  # Zwróć listę identyfikatorów wiadomości
    

