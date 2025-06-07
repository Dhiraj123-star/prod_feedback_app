from fastapi import FastAPI
from app.routes import auth,feedback

app = FastAPI(title="Production Grade Feedback System")

app.include_router(auth.router)
app.include_router(feedback.router)
