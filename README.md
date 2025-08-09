# AI News Summarizer - Text Summarization

A Python-based web application that automatically fetches news articles from URLs and generates concise summaries using Google's Gemini AI model. The application provides both a standalone script and a FastAPI web service.

## Features

- **Web Scraping**: Extracts article content from news URLs
- **Content Cleaning**: Removes HTML, CSS, and JavaScript from scraped content
- **AI Summarization**: Uses Google Gemini 2.0 Flash model for intelligent text summarization
- **REST API**: FastAPI-based web service for easy integration
- **CORS Support**: Configured for frontend integration

## Project Structure

```
AI-New-Summarizer-Text-Summarization/
├── newsummarizer.py      # Core summarization functions
├── main.py              # FastAPI web service
└── README.md           # Project documentation
```

## Prerequisites

- Python 3.7+
- Google AI API key (Gemini)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd AI-New-Summarizer-Text-Summarization
   ```

2. **Install required dependencies**:
   ```bash
   pip install requests beautifulsoup4 google-genai fastapi uvicorn
   ```

3. **Set up Google AI API**:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Replace the API key in the code with your own key

## Usage

### Standalone Script

The `newsummarizer.py` file can be run directly to summarize a single article:

```python
python newsummarizer.py
```

This will process the hardcoded URL and print the summary to the console.

### Web API Service

1. **Start the FastAPI server**:
   ```bash
   python main.py
   ```

2. **The API will be available at**: `http://127.0.0.1:8000`

3. **API Documentation**: Visit `http://127.0.0.1:8000/docs` for interactive API documentation

### API Endpoints

#### POST `/process_url`

Summarizes content from a given URL.

**Request Body**:
```json
{
  "url": "https://example-news-site.com/article"
}
```

**Response**:
```json
{
  "result": "AI-generated summary of the article content..."
}
```

**Example using curl**:
```bash
curl -X POST "http://127.0.0.1:8000/process_url" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://edition.cnn.com/2025/04/01/middleeast/israel-strikes-beirut-hezbollah-intl-hnk/index.html"}'
```

## Core Functions

### `process_url(url: str)`
- Fetches HTML content from the provided URL
- Extracts paragraph text using BeautifulSoup
- Returns raw text content

### `clean_html_css_js(text: str)`
- Removes JavaScript `<script>` tags
- Removes CSS `<style>` tags
- Strips HTML tags
- Normalizes whitespace

### `summarize_text(text: str)`
- Sends cleaned text to Google Gemini AI
- Returns AI-generated summary

## Configuration

### CORS Settings
The API is configured to accept requests from `http://127.0.0.1:3000`. Update the `allow_origins` in `main.py` to match your frontend URL:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://your-frontend-url.com"],
    # ... other settings
)
```

### API Key Security
⚠️ **Important**: The current implementation has the API key hardcoded. For production use, consider:

1. Using environment variables:
   ```python
   import os
   api_key = os.getenv('GOOGLE_AI_API_KEY')
   ```

2. Using a configuration file
3. Using cloud secret management services

## Dependencies

- `requests`: HTTP library for fetching web content
- `beautifulsoup4`: HTML parsing and content extraction
- `google-genai`: Google Gemini AI client
- `fastapi`: Modern web framework for building APIs
- `uvicorn`: ASGI server for FastAPI
- `pydantic`: Data validation using Python type annotations

## Error Handling

The application includes basic error handling, but consider adding:
- Network timeout handling
- Invalid URL validation
- API rate limiting
- Content length validation
- Error logging

## Limitations

- Currently optimized for news articles with paragraph tags (`<p>`)
- Requires internet connection for both web scraping and AI processing
- Limited to websites that allow scraping
- API key exposed in source code (security concern)

## Future Enhancements

- [ ] Environment-based configuration
- [ ] Support for more content types (beyond paragraphs)
- [ ] Batch processing multiple URLs
- [ ] Caching mechanism
- [ ] Rate limiting
- [ ] User authentication
- [ ] Database integration for storing summaries
- [ ] Support for other AI models

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request


## Support

For issues and questions, please [create an issue](link-to-issues) in the repository.
