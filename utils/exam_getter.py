from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


class Traditional:
    def __init__(self):
        cluster = os.getenv("CLUSTER")
        uri = cluster
        client = MongoClient(uri)
        self.collection = client['examotion']['traditional']

    def add_data(self, data):
        result = self.collection.insert_one(data)
        print(result)
