from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
import re


load_dotenv()

# Get the API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY. Set it in your environment variables.")

# Initialize Gemini client
try:
    client = genai.Client(api_key=GOOGLE_API_KEY)
except Exception as e:
    raise RuntimeError(f"Failed to initialize Gemini API client: {str(e)}")


def clean_html_css_js(text):
    """Removes HTML, CSS, and JavaScript from a string."""
    try:
        text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)  # Remove JavaScript
        text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)  # Remove CSS
        text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
        text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
        return text
    except Exception as e:
        print(f"Error cleaning text: {str(e)}")
        return text  # Return raw text if cleaning fails


def process_url(url: str):
    """Fetches and extracts text content from a webpage."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error for HTTP failures (4xx, 5xx)

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("p")
        text = " ".join([p.get_text() for p in articles])

        if not text.strip():
            raise ValueError("No readable text found on the page.")

        return text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {str(e)}")
        return None  # Return None if request fails


def summarize_text(text):
    """Summarizes text using Gemini API."""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are to summarize the content."
            ),
            contents=[text]  # Gemini expects a list, not a string
        )

        if not response or not response.candidates:
            raise ValueError("Empty response from Gemini API.")

        return response.candidates[0].content  # Extract summary
    except Exception as e:
        print(f"Error summarizing text: {str(e)}")
        return "Summary could not be generated."
