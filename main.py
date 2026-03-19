from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

app = FastAPI()

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
