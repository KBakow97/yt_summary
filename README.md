# YouTube Video Summarizer API
This project provides a powerful API for generating concise summaries from YouTube videos. By utilizing FastAPI and advanced natural language processing models, it efficiently processes a YouTube link, retrieves the video transcript, and generates a summary. The summarized content is then sent directly to the user's phone via WhatsApp using Twilio's messaging API.

Key Features
YouTube Video Input: The API accepts a YouTube URL.
Transcript Retrieval: Extracts the video's transcript using the YouTubeTranscriptApi, supporting multiple languages (Polish and English by default).
## Summary Generation:
Hugging Face Model: Utilizes the **facebook/bart-large-cnn** model from Hugging Face for summarizing video transcripts.

**OpenAI GPT-4**: As an alternative, it offers summary generation using OpenAI's GPT-4 model, providing in-depth analysis and summarization.
Twilio WhatsApp Integration: The generated summary is delivered directly to the user's phone via WhatsApp using Twilio, providing a seamless mobile experience.

## Environment Variables
To run this project, you need to create a .env file with the following keys:

- OPENAI_API_KEY=your_openai_api_key
- TWILIO_SID=your_twilio_sid
- TWILIO_AUTH=your_twilio_auth_token
- WHATSAPP_NR=your_twilio_whatsapp_number
These keys are essential for both generating summaries (via OpenAI) and sending them through WhatsApp using Twilio's messaging service.

## How It Works
Submit a YouTube Video URL: The user provides a YouTube video link through the API.
URL Validation and Extraction: The URL is validated and processed to extract the video ID. Invalid URLs are rejected with an appropriate error message.
Transcript Retrieval: Using YouTubeTranscriptApi, the video transcript is fetched in supported languages (Polish and English).
Summary Generation: The transcript is analyzed and summarized using one of two available models:
Hugging Face facebook/bart-large-cnn for concise, high-quality summaries.
OpenAI GPT-4 for more complex and insightful summaries.
WhatsApp Delivery: The generated summary is sent to the provided phone number via WhatsApp using Twilio, making the content easily accessible.

## Requirements
All necessary dependencies are listed in the **requirements.txt** file, and can be installed with:

`pip install -r requirements.txt`
Technologies Used
**FastAPI**: The core web framework for building and managing API requests.

**Hugging Face Transformers**: Specifically the facebook/bart-large-cnn model for natural language summarization.

**OpenAI GPT-4**: An additional summarization option for richer, more detailed summaries.

**Twilio API**: For sending the generated summaries to WhatsApp, providing real-time delivery to mobile devices.

**YouTube Transcript API**: To extract transcripts directly from YouTube videos.

## Transcript Extraction Logic
The project uses the YouTubeTranscriptApi to fetch video transcripts. Here's how the process works:

The URL is validated to ensure it's a valid YouTube link.
The transcript is fetched for supported languages (pl and en).
If no transcript is found, an error is raised.

### How to Run
Clone the repository:

`git clone <repository-url>`
Install dependencies:

`pip install -r requirements.txt`
Add your .env file with the necessary API keys.

Run the FastAPI server:

`uvicorn app.main:app --reload`
Submit a YouTube video URL via the API, and receive the generated summary on WhatsApp.

