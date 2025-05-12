from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Competitor, Base
from app.db import SessionLocal, engine

router = APIRouter(prefix="/competitors", tags=["Competitors"])

# Ensure tables exist
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("")
def list_competitors(db: Session = Depends(get_db)):
    competitors = db.query(Competitor).all()
    return [
        {"id": c.id, "name": c.name, "website": c.website, "linkedin": c.linkedin}
        for c in competitors
    ]

@router.post("")
def add_competitor(name: str, website: str, linkedin: str = "", db: Session = Depends(get_db)):
    competitor = Competitor(name=name, website=website, linkedin=linkedin)
    db.add(competitor)
    db.commit()
    db.refresh(competitor)
    return {"id": competitor.id, "name": competitor.name, "website": competitor.website, "linkedin": competitor.linkedin}

    return [
        {"id": c.id, "name": c.name, "website": c.website, "linkedin": c.linkedin}
        for c in competitors
    ]

@router.post("")
def add_competitor(name: str, website: str, linkedin: str = "", db: Session = Depends(get_db)):
    competitor = Competitor(name=name, website=website, linkedin=linkedin)
    db.add(competitor)
    db.commit()
    db.refresh(competitor)
    return {"id": competitor.id, "name": competitor.name, "website": competitor.website, "linkedin": competitor.linkedin}
