from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class DateIdea(Base):
    __tablename__ = "dates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    budget = Column(String)
    likes = Column(Integer, default=0)
    # Relationship to reviews
    reviews = relationship("Review", back_populates="date")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    date_id = Column(Integer, ForeignKey("dates.id"))
    date = relationship("DateIdea", back_populates="reviews")
