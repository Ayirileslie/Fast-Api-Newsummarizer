from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from newsummarizer import clean_html_css_js, process_url, summarize_text

app = FastAPI()

# CORS settings (update for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

@app.post("/process_url")
async def process_url_api(request: URLRequest):
    url = request.url.strip()
    if not url:
        raise HTTPException(status_code=400, detail="URL cannot be empty.")

    result = process_url(url)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to fetch content from the URL.")

    cleaned_text = clean_html_css_js(result)
    if not cleaned_text:
        raise HTTPException(status_code=500, detail="Failed to clean extracted text.")

    summary = summarize_text(cleaned_text)
    if not summary:
        raise HTTPException(status_code=500, detail="Failed to generate summary.")

    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
