from transformers import pipeline
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document  
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

def split_text(content:str, max_lenght: int= 1024):
    words = content.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_length += len(word) +1 # for space
        if current_length > max_lenght:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) +1
        else:
            current_chunk.append(word)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def model_summarization(content:str):
    #test_content = "This is a short text for testing summarization."
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    chunks = split_text(content, max_lenght=1024)
    summaries = []
    for chunk in chunks:
        print(chunk)
        model_sum = summarizer(chunk)[0]['summary_text']
        summaries.append(model_sum)

    full_summary = " ".join(summaries)
    return full_summary


def model_summarization_openai(content: str):
    llm = ChatOpenAI(model="gpt-4")
    
    prompt = ChatPromptTemplate.from_messages(
        [("system", "Write a concise summary of the following information in the language in which you received it:\n\n{context}")]
    )

    chain = create_stuff_documents_chain(llm, prompt)

    document = Document(page_content=content)

    result = chain.invoke({"context": [document]})
    
    return result