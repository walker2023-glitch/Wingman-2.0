from database import SessionLocal, init_db
from models import DateIdea

# Initialize the tables
init_db()
db = SessionLocal()

# Your Rexburg data parsed into Python objects
raw_data = [
    {"name": "Mini Golf at FatCats", "description": "Play a round of mini golf...", "category": "Games/Activities", "budget": "$$"},
    {"name": "Ice Cream at Kiwi Loco", "description": "Build your own frozen yogurt...", "category": "Food", "budget": "$"},
    # ... Add 3-4 more here to test, or the whole list later
]

for item in raw_data:
    date = DateIdea(**item)
    db.add(date)

db.commit()
db.close()
print("Database Seeded! 🚀")
