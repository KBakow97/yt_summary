from transformers import pipeline
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document  
import os

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

def split_text(content: str, max_length: int = 1024) -> list[str]:
    """Splits text into smaller chunks based on a maximum length."""
    words = content.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_length += len(word) + 1  # Adding space length
        if current_length > max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1
        else:
            current_chunk.append(word)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def model_summarization(content: str) -> str:
    """Generates a summary for the given content using a pre-trained BART model."""
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    chunks = split_text(content, max_length=1024)
    summaries = [summarizer(chunk)[0]['summary_text'] for chunk in chunks]
    return " ".join(summaries)

def model_summarization_openai(content: str) -> str:
    """Generates a summary using OpenAI's GPT-4 model."""
    llm = ChatOpenAI(model="gpt-4")

    prompt = ChatPromptTemplate.from_messages(
        [("system", "Write a concise summary of the following information in the language in which you received it:\n\n{context}")]
    )

    chain = create_stuff_documents_chain(llm, prompt)
    document = Document(page_content=content)
    result = chain.invoke({"context": [document]})
    
    return result.content

def analyze_sentiment(content: str) -> str:
    """Analyzes the sentiment of the provided text using OpenAI's GPT-4 model."""
    llm = ChatOpenAI(model="gpt-4")

    prompt = ChatPromptTemplate.from_messages(
        [("system", "Analyze the sentiment of the following text. Answer in the language that the summary was given. Return 'positive', 'neutral', or 'negative'. Text:\n\n{context}")]
    )
    
    chain = prompt | llm
    result = chain.invoke({"context": content})

    return result.content

def detect_topics(text: str) -> str:
    """Extracts up to 3 main topics from the text using OpenAI's GPT-4 model."""
    llm = ChatOpenAI(model="gpt-4")

    prompt = ChatPromptTemplate.from_messages(
        [("system", "Analyze the following text and extract up to 3 main topics mentioned. Answer in the language that the summary was given:\n\n{context}")]
    )

    chain = prompt | llm
    document = Document(page_content=text)
    result = chain.invoke({"context": document.page_content})
    
    return result.content
