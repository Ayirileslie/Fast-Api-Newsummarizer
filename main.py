from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
import re
from fastapi.middleware.cors import CORSMiddleware

from newsummarizer import clean_html_css_js,process_url,summarize_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class URLRequest(BaseModel):
    url: str

@app.post("/process_url")
async def process_url_api(request: URLRequest):
    result = process_url(request.url)
    print("Fetched Content:", result)  # Debugging

    result2 = clean_html_css_js(result)
    print("Cleaned Content:", result2)  # Debugging

    result3 = summarize_text(result2)
    print("Summary:", result3)  # Debugging

    return {"result": result3}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
