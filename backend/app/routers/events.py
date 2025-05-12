from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app import scraper, summarizer, charting
from app.scraper_news import scrape_news
from app.scraper_linkedin import scrape_linkedin
from app.models import Event, Base
from app.db import SessionLocal, engine
from app.emailer import send_email

router = APIRouter(prefix="/events", tags=["Events"])

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/scrape")
def scrape_and_summarize(
    url: str = Query(None, description="Competitor website URL to scrape"),
    news_url: str = Query(None, description="News website URL to scrape"),
    linkedin: str = Query(None, description="Company name for LinkedIn scraping"),
    db: Session = Depends(get_db)
):
    events = []
    if url:
        events += scraper.scrape_website(url)
    if news_url:
        events += scrape_news(news_url)
    if linkedin:
        events += scrape_linkedin(linkedin)
    summary = summarizer.summarize_events(events)
    # Store events in DB
    for ev in events:
        e = Event(competitor_id=1, type=ev.get('type', 'News'), headline=ev.get('headline'), url=ev.get('url', ''), summary=summary)
        db.add(e)
    db.commit()
    return {"events": events, "summary": summary}

@router.get("")
def list_events(db: Session = Depends(get_db)):
    db_events = db.query(Event).all()
    events = [
        {"id": e.id, "competitor_id": e.competitor_id, "type": e.type, "headline": e.headline, "url": e.url, "summary": e.summary, "timestamp": e.timestamp}
        for e in db_events
    ]
    chart_html = charting.generate_trend_chart(events)
    return {"events": events, "trend_chart_html": chart_html}

@router.post("/send_report")
def send_report(recipient: str, db: Session = Depends(get_db)):
    db_events = db.query(Event).all()
    events = [
        {"type": e.type, "headline": e.headline, "summary": e.summary, "timestamp": e.timestamp}
        for e in db_events
    ]
    summary = '\n'.join([e["headline"] for e in events if e["headline"]])
    chart_html = charting.generate_trend_chart(events)
    body = f"Summary of recent competitor events:\n\n{summary}\n\nTrend Chart (open in browser):\n{chart_html}"
    subject = "CompetiScan: Competitor Intelligence Report"
    send_email(subject, body, [recipient])
    return {"status": "sent", "recipient": recipient}
