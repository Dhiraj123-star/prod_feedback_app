from fastapi import APIRouter

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.get("/status")
def feedback_status():
    return {"status": "Feedback route working"}
