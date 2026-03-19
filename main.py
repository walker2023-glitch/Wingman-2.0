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
