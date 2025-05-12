from fastapi import FastAPI
from routers import competitors, events, summaries

app = FastAPI(title="CompetiScan: AI Competitor Intelligence Tracker")

app.include_router(competitors.router)
app.include_router(events.router)
app.include_router(summaries.router)

@app.get("/")
def root():
    return {"message": "Welcome to CompetiScan!"}
