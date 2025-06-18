# 🌐 AI-Powered Web Article Summarizer API

An API built with **FastAPI**, **BeautifulSoup**, and **Google Gemini Pro** to extract and summarize web content from user-submitted URLs. Designed to power frontend apps (e.g. Next.js) with real-time summarization functionality.

---

## 🧠 Overview

This backend service allows users to paste any URL (news, blog post, documentation, etc.) and receive a clean, AI-generated summary of the content. The pipeline combines web scraping, text cleaning, and LLM summarization to deliver concise, human-readable results.

---

## 🎯 Problem Statement

The average user is overwhelmed by the volume of information available online. Reading full-length articles isn't always feasible, especially on mobile. This API aims to:
- Scrape and sanitize article content
- Use Google’s Gemini to generate fast and accurate summaries
- Integrate seamlessly into web interfaces like dashboards, AI tools, or extensions

---

## 🚀 How It Works

1. A **Next.js frontend** sends a POST request with a URL.
2. The API:
   - Fetches the HTML content from the URL.
   - Cleans it using `BeautifulSoup` to remove scripts, CSS, and tags.
   - Summarizes the text using **Google Gemini Pro API**.
3. A summarized version of the content is returned.

---

## 🔁 Endpoint

### `POST /process_url`

#### ✅ Request Body

```json
{
  "url": "https://example.com/sample-article"
}
