from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


class ExamPageModel:
    def __init__(self, user_data):
        cluster = os.getenv("CLUSTER")
        uri = cluster
        client = MongoClient(uri)
        self.collection = client['examotion']['test']

    def get_specific_data(self, name):
        # find documents
        result = self.collection.find_one({"name": f"{name}"})
        # print results
        print("Document found:\n", result)


model = ExamPageModel("test")
model.get_specific_data("Julius")
