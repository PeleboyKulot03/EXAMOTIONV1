from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
cluster = os.getenv("CLUSTER")
uri = cluster
client = MongoClient(uri)
collection = client['examotion']['students']

result = list(collection.find({'from': 'guarin'}))
emotions = ['Neutral', 'Excited', 'Bored', 'Nervous', 'Frustrated', 'Surprised']

test = []
for item in result:
    result = list(collection.find({'name': item['name']}))
    time = result[0]['time']
    minutes = time // 60
    seconds = time % 60
    print(f"{minutes:02}:{seconds:02}")
