import os
import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
import re

# Get the API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def clean_html_css_js(text):
    # Remove JavaScript (scripts)
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)

    # Remove CSS (style blocks)
    text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove extra whitespace, newlines, and tabs
    text = re.sub(r'\s+', ' ', text).strip()

    return text
def process_url(url: str):
      response = requests.get(url)
      soup = BeautifulSoup(response.text, "html.parser")
      articles = soup.find_all("p")
      text = " ".join([p.get_text() for p in articles])

      return text
    


def summarize_text(text):
 

        client = genai.Client(api_key=GOOGLE_API_KEY)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are to summarize the content ."),
            contents=text
        )

        return(response.text)


result=process_url(url)
result2=clean_html_css_js(result)

result3=summarize_text(result2)

print(result3)