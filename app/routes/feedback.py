from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models import Feedback, FeedbackCreate, FeedbackResponse
from app.database import get_db
from app.routes.auth import get_current_user  # assuming you have this already

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/", response_model=FeedbackResponse)
def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_feedback = Feedback(
        content=feedback.content,
        owner_id=current_user["email"]  # Store CouchDB email
    )
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback


@router.get("/", response_model=List[FeedbackResponse])
def get_feedbacks(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return db.query(Feedback).filter(Feedback.owner_id == current_user["email"]).all()


@router.put("/{feedback_id}", response_model=FeedbackResponse)
def update_feedback(
    feedback_id: int,
    feedback: FeedbackCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    feedback_obj = db.query(Feedback).filter(
        Feedback.id == feedback_id,
        Feedback.owner_id == current_user["email"]
    ).first()

    if not feedback_obj:
        raise HTTPException(status_code=404, detail="Feedback not found or unauthorized")

    feedback_obj.content = feedback.content
    db.commit()
    db.refresh(feedback_obj)
    return feedback_obj


@router.delete("/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feedback(
    feedback_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    feedback_obj = db.query(Feedback).filter(
        Feedback.id == feedback_id,
        Feedback.owner_id == current_user["email"]
    ).first()

    if not feedback_obj:
        raise HTTPException(status_code=404, detail="Feedback not found or unauthorized")

    db.delete(feedback_obj)
    db.commit()
