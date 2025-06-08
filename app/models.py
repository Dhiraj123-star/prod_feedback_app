from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Pydantic Models
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# SQLAlchemy Feedback Table
class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(String, nullable=False)  # CouchDB user ID or email

# Pydantic Models for Feedback
class FeedbackCreate(BaseModel):
    content: str

class FeedbackResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    owner_id: str  # Match with CouchDB user ID/email

    model_config = ConfigDict(from_attributes=True)  # Pydantic v2 fix
