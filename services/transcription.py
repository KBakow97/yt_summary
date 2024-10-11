from fastapi import HTTPException
from youtube_transcript_api import YouTubeTranscriptApi


def url_checking(url:str):
    if "youtube.com" in url or "youtu.be" in url:
        return url.split("v=")[-1] if "v=" in url else url.split("/")[-1]
    else:
        return HTTPException(status_code=400, detail="Invalid Youtube URL")


def transcript(video_id):
    try:
        text = ""
        yt = YouTubeTranscriptApi.get_transcript(video_id, languages=['pl','en'])
        for data in yt:
            text += data['text'] + " "
        return text
    except yt == None:
        return HTTPException(status_code=400, detail="No transcription")