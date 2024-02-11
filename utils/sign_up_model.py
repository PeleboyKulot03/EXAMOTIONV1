from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os


class SignUpModel:
    def __init__(self, username, password):
        load_dotenv()
        self.username = username
        self.password = password
        cluster = os.getenv("CLUSTER")
        uri = cluster
        self.client = MongoClient(uri)
        self.collection = self.client['examotion']['credentials']

    def sign_up(self):
        user = self.collection.find_one({"username": self.username})
        if user is not None:
            return False, "Sorry username is already used!"

        else:
            my_db = self.client['examotion']
            collist = my_db.list_collection_names()
            if self.username in collist:
                return False, "Sorry username is already used!"
            else:
                data = {"username": self.username,
                        "password": self.password}
                try:
                    self.collection.insert_one(data)
                    return True, "Sorry, an error occurred, Please try again later!"

                except Exception as e:
                    return False, "Sorry, ", e
