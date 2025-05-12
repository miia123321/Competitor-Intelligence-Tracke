from fastapi import APIRouter

router = APIRouter(prefix="/summaries", tags=["Summaries"])

@router.get("")
def get_summaries():
    return [
        {"id": 1, "summary": "Competitor A launched new product X. Competitor B hired new CTO."}
    ]
