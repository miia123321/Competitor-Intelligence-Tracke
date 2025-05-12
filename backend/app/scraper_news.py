import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def scrape_news(url: str) -> List[Dict]:
    """Scrape latest news headlines from a news website."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        news_items = []
        # Example: select top headlines from a news site
        for item in soup.select('h2, h3'):
            text = item.get_text(strip=True)
            if text:
                news_items.append({"headline": text})
        return news_items[:8]
    except Exception as e:
        return [{"error": str(e)}]
