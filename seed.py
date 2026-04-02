from database import SessionLocal, init_db
from models import DateIdea
import os

# 1. Clean start: Optional, but recommended to avoid duplicates
# If you want to start fresh, uncomment the line below:
# if os.path.exists("test.db"): os.remove("test.db")

# Initialize the tables
init_db()
db = SessionLocal()

raw_data = [
    {
        "name": "Mini Golf at FatCats", 
        "description": "Play a round of mini golf, challenge each other at the arcade, and see who wins the most tickets.", 
        "category": "Games/Activities", "budget": "$$", "location": "FatCats Rexburg", 
        "needs_car": True, "dateType": "both", "duration": "2hr", "hasStudentDiscount": True
    },
    {
        "name": "Ice Cream at Kiwi Loco", 
        "description": "Build your own frozen yogurt with a mountain of toppings.", 
        "category": "Food", "budget": "$", "location": "Kiwi Loco", 
        "needs_car": False, "dateType": "both", "duration": "1hr", "hasStudentDiscount": False
    },
    {
        "name": "Temple Grounds Walk", 
        "description": "A peaceful evening walk around the Rexburg Idaho Temple grounds.", 
        "category": "Spiritual", "budget": "$", "location": "Rexburg Temple", 
        "needs_car": False, "dateType": "single", "duration": "1hr", "hasStudentDiscount": False
    },
    {
        "name": "Dance Night at BYUI", 
        "description": "Swing and country on Wednesdays, ballroom and Latin on Fridays.", 
        "category": "Entertainment", "budget": "$", "location": "MC Ballroom", 
        "needs_car": False, "dateType": "both", "duration": "2hr", "hasStudentDiscount": True
    },
    {
        "name": "Movie Night with Redbox", 
        "description": "Rent a movie from Redbox, pop some popcorn, and cozy up.", 
        "category": "At Home", "budget": "$", "location": "At Home", 
        "needs_car": False, "dateType": "single", "duration": "2hr", "hasStudentDiscount": False
    },
    {
        "name": "Board Games Night", 
        "description": "Break out Ticket to Ride or Catan. Perfect with 4–8 players.", 
        "category": "At Home", "budget": "$", "location": "At Home", 
        "needs_car": False, "dateType": "group", "duration": "3hr", "hasStudentDiscount": False
    },
    {
        "name": "Dinner at Craigo's Pizza", 
        "description": "Grab a pizza and breadsticks at a Rexburg staple.", 
        "category": "Food", "budget": "$$", "location": "Craigo's", 
        "needs_car": True, "dateType": "both", "duration": "1hr", "hasStudentDiscount": True
    },
    {
        "name": "Hike to Kelly Canyon", 
        "description": "Drive out for a scenic hike or skiing in the winter.", 
        "category": "Outdoor", "budget": "$$$", "location": "Kelly Canyon", 
        "needs_car": True, "dateType": "both", "duration": "halfday", "hasStudentDiscount": False
    },
    {
        "name": "Cook a New Recipe Together", 
        "description": "Pick a fun recipe online and shop for ingredients together.", 
        "category": "At Home", "budget": "$$", "location": "Kitchen", 
        "needs_car": False, "dateType": "single", "duration": "2hr", "hasStudentDiscount": False
    },
    {
        "name": "Stargazing at the Rexburg Mesa", 
        "description": "Clear night skies away from city lights. Bring hot cocoa.", 
        "category": "Outdoor", "budget": "$", "location": "The Mesa", 
        "needs_car": True, "dateType": "single", "duration": "1hr", "hasStudentDiscount": False
    },
    {
        "name": "Ice Skating at Rexburg Rapids", 
        "description": "Lace up and glide around the ice rink at Rexburg Rapids.", 
        "category": "Games/Activities", "budget": "$$", "location": "Rexburg Rapids", 
        "needs_car": True, "dateType": "both", "duration": "2hr", "hasStudentDiscount": False
    },
    {
        "name": "The Righteous Slice", 
        "description": "Share a Neapolitan Bee Sting pizza in a laid-back atmosphere.", 
        "category": "Food", "budget": "$$", "location": "Righteous Slice", 
        "needs_car": False, "dateType": "single", "duration": "1hr", "hasStudentDiscount": False
    },
    {
        "name": "Civil Defense Caves Hike", 
        "description": "A 4-mile hike out to the eerie lava tube caves.", 
        "category": "Outdoor", "budget": "$", "location": "North Rexburg", 
        "needs_car": True, "dateType": "group", "duration": "halfday", "hasStudentDiscount": False
    },
    {
        "name": "Laser Tag at BYUI", 
        "description": "BYU-Idaho's Laser Tag arena offers fast-paced group fun.", 
        "category": "Games/Activities", "budget": "$", "location": "Hart Building", 
        "needs_car": False, "dateType": "group", "duration": "1hr", "hasStudentDiscount": True
    },
    {
        "name": "Sand Castles at the Dunes", 
        "description": "Head to the sand dunes with buckets of water.", 
        "category": "Outdoor", "budget": "$", "location": "St. Anthony Dunes", 
        "needs_car": True, "dateType": "both", "duration": "3hr", "hasStudentDiscount": False
    },
    {
        "name": "Dairy Queen Treat + Walk", 
        "description": "Grab Blizzards and take a relaxed walk on the campus loop.", 
        "category": "Food", "budget": "$", "location": "Dairy Queen", 
        "needs_car": False, "dateType": "single", "duration": "1hr", "hasStudentDiscount": False
    },
    {
        "name": "The Hickory Dinner Date", 
        "description": "Classic BBQ dinner date. Try something new on the menu.", 
        "category": "Food", "budget": "$$$", "location": "The Hickory", 
        "needs_car": False, "dateType": "single", "duration": "2hr", "hasStudentDiscount": False
    },
    {
        "name": "Red Rabbit Grill", 
        "description": "A calm stroll and a real dinner-date vibe.", 
        "category": "Food", "budget": "$$$", "location": "Red Rabbit Grill", 
        "needs_car": True, "dateType": "single", "duration": "2hr", "hasStudentDiscount": False
    },
    {
        "name": "Swig Soda Run", 
        "description": "Grab custom sodas and do a cozy car chat session.", 
        "category": "Food", "budget": "$", "location": "Swig Rexburg", 
        "needs_car": True, "dateType": "both", "duration": "1hr", "hasStudentDiscount": False
    }
]

for item in raw_data:
    # Check if entry exists to avoid duplicates if you don't delete the .db
    exists = db.query(DateIdea).filter(DateIdea.name == item["name"]).first()
    if not exists:
        date = DateIdea(**item)
        db.add(date)

db.commit()
db.close()
print("Database Seeded with all 19 dates! 🚀")
