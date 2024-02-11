from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


class ExamPageModel:
    def __init__(self):
        cluster = os.getenv("CLUSTER")
        uri = cluster
        client = MongoClient(uri)
        self.collection = client['examotion']['students']

    def add_data(self, data):
        result = self.collection.insert_one(data)
        print(result)
