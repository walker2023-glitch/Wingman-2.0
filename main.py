from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles # 1. ADD THIS IMPORT
from sqlalchemy.orm import Session
from database import SessionLocal
import models

app = FastAPI()

# 2. ADD THIS LINE RIGHT HERE
app.mount("/static", StaticFiles(directory="static"), name="static")

# ... rest of your code ...
# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/dates")
def get_dates(db: Session = Depends(get_db)):
    return db.query(models.DateIdea).all()


from pydantic import BaseModel

# A simple tool to validate the data coming from the website
class PostCreate(BaseModel):
    content: str
    date_id: int

@app.post("/api/dates/{date_id}/like")
def like_date(date_id: int, db: Session = Depends(get_db)):
    date = db.query(models.DateIdea).filter(models.DateIdea.id == date_id).first()
    date.likes += 1
    db.commit()
    return {"likes": date.likes}

@app.post("/api/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(content=post.content, date_id=post.date_id)
    db.add(new_post)
    db.commit()
    return {"status": "success"}

@app.get("/api/posts/{date_id}")
def get_posts(date_id: int, db: Session = Depends(get_db)):
    return db.query(models.Post).filter(models.Post.date_id == date_id).all()


import math # Add this to your imports at the top

class PredictionInput(BaseModel):
    interests: int
    hours: int
    notice: int
    people: int

@app.post("/api/predict")
def predict_success(data: PredictionInput):
    # Your R Model Coefficients
    b0, b1, b2, b3, b4 = -5.671, 0.322, 0.111, 0.344, -0.389
    
    logit = b0 + (b1 * data.interests) + (b2 * data.hours) + (b3 * data.notice) + (b4 * data.people)
    prob = 1 / (1 + math.exp(-logit))
    
    return {"chance": f"{round(prob * 100, 1)}%"}

@app.post("/api/dates/{date_id}/like")
def like_date(date_id: int, db: Session = Depends(get_db)):
    date = db.query(models.DateIdea).filter(models.DateIdea.id == date_id).first()
    if date:
        date.likes += 1
        db.commit()
        db.refresh(date) # This updates the object with the new count
        return {"likes": date.likes}
    return {"error": "Date not found"}
