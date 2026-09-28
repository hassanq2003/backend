import os
import urllib.parse
from datetime import datetime, timezone, timedelta
from pymongo import MongoClient

# Get password or use the provided one
password = urllib.parse.quote_plus('daniyal@2003')
uri = f'mongodb+srv://i233029:{password}@project.h2qh5gr.mongodb.net/?appName=PROJECT'

print("Connecting to MongoDB...")
client = MongoClient(uri)
db = client['tactiq_db']
collection = db['api_phone']

print("Inserting demo data...")
demo_data = [
    {
        "name": "John's iPhone",
        "sync_time": datetime.now(timezone.utc) - timedelta(hours=2),
        "created_at": datetime.now(timezone.utc)
    },
    {
        "name": "Sarah's Pixel",
        "sync_time": datetime.now(timezone.utc) - timedelta(minutes=15),
        "created_at": datetime.now(timezone.utc)
    },
    {
        "name": "Office Test Device",
        "sync_time": datetime.now(timezone.utc) - timedelta(days=1),
        "created_at": datetime.now(timezone.utc)
    }
]

result = collection.insert_many(demo_data)
print(f"Successfully inserted {len(result.inserted_ids)} records!")
