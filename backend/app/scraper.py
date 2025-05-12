import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def scrape_website(url: str) -> List[Dict]:
    """Scrape a competitor's website for news or updates."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        # Example: scrape headlines and links from a news section
        news_items = []
        for item in soup.find_all('a', limit=5):
            text = item.get_text(strip=True)
            href = item.get('href')
            if text and href:
                news_items.append({"headline": text, "url": href})
        return news_items
    except Exception as e:
        return [{"error": str(e)}]

# Example usage:
if __name__ == "__main__":
    print(scrape_website("https://techcrunch.com/"))
