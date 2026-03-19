from database import SessionLocal, init_db
from models import DateIdea

# Initialize the tables
init_db()
db = SessionLocal()

# Your Rexburg data parsed into Python objects
    raw_data = [
    {"name": "Mini Golf at FatCats", "description": "Play a round of mini golf, challenge each other at the arcade, and see who wins the most tickets.", "category": "Games/Activities", "budget": "$$"},
    {"name": "Ice Cream at Kiwi Loco", "description": "Build your own frozen yogurt with a mountain of toppings.", "category": "Food", "budget": "$"},
    {"name": "Temple Grounds Walk", "description": "A peaceful evening walk around the Rexburg Idaho Temple grounds.", "category": "Spiritual", "budget": "$"},
    {"name": "Dance Night at BYUI", "description": "Swing and country on Wednesdays, ballroom and Latin on Fridays.", "category": "Entertainment", "budget": "$"},
    {"name": "Movie Night with Redbox", "description": "Rent a movie from Redbox, pop some popcorn, and cozy up.", "category": "At Home", "budget": "$"},
    {"name": "Board Games Night", "description": "Break out Ticket to Ride or Catan. Perfect with 4–8 players.", "category": "At Home", "budget": "$"},
    {"name": "Dinner at Craigo's Pizza", "description": "Grab a pizza and breadsticks at a Rexburg staple.", "category": "Food", "budget": "$$"},
    {"name": "Hike to Kelly Canyon", "description": "Drive out for a scenic hike or skiing in the winter.", "category": "Outdoor", "budget": "$$$"},
    {"name": "Cook a New Recipe Together", "description": "Pick a fun recipe online and shop for ingredients together.", "category": "At Home", "budget": "$$"},
    {"name": "Stargazing at the Rexburg Mesa", "description": "Clear night skies away from city lights. Bring hot cocoa.", "category": "Outdoor", "budget": "$"},
    {"name": "Ice Skating at Rexburg Rapids", "description": "Lace up and glide around the ice rink at Rexburg Rapids.", "category": "Games/Activities", "budget": "$$"},
    {"name": "The Righteous Slice", "description": "Share a Neapolitan Bee Sting pizza in a laid-back atmosphere.", "category": "Food", "budget": "$$"},
    {"name": "Civil Defense Caves Hike", "description": "A 4-mile hike out to the eerie lava tube caves.", "category": "Outdoor", "budget": "$"},
    {"name": "Laser Tag at BYUI", "description": "BYU-Idaho's Laser Tag arena offers fast-paced group fun.", "category": "Games/Activities", "budget": "$"},
    {"name": "Sand Castles at the Dunes", "description": "Head to the sand dunes with buckets of water.", "category": "Outdoor", "budget": "$"},
    {"name": "Dairy Queen Treat + Walk", "description": "Grab Blizzards and take a relaxed walk on the campus loop.", "category": "Food", "budget": "$"},
    {"name": "The Hickory Dinner Date", "description": "Classic BBQ dinner date. Try something new on the menu.", "category": "Food", "budget": "$$$"},
    {"name": "Red Rabbit Grill", "description": "A calm stroll and a real dinner-date vibe.", "category": "Food", "budget": "$$$"},
    {"name": "Swig Soda Run", "description": "Grab custom sodas and do a cozy car chat session.", "category": "Food", "budget": "$"}
]


for item in raw_data:
    date = DateIdea(**item)
    db.add(date)

db.commit()
db.close()
print("Database Seeded! 🚀")
