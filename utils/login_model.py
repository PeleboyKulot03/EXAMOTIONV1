from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os


class LoginPageModel:
    def __init__(self, username, password):
        load_dotenv()
        self.username = username
        self.password = password
        cluster = os.getenv("CLUSTER")
        uri = cluster
        client = MongoClient(uri)
        self.collection = client['examotion']['test_credentials']

    def login(self):
        user = self.collection.find_one({"username": self.username})
        if user is None:
            return False
        else:
            if user['username'] == self.username and user['password'] == self.password:
                print("hey")
                return True
            else:
                print("sad")
                return False

