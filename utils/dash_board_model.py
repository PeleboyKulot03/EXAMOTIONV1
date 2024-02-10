from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from statics import static

stats = static.Statics()
answer_key = stats.get_answer_key()
load_dotenv()
emotions = ['Neutral', 'Excited', 'Bored', 'Nervous', 'Frustrated', 'Confused', 'Surprised']


class DashBoardModel:
    def __init__(self):
        cluster = os.getenv("CLUSTER")
        uri = cluster
        client = MongoClient(uri)
        self.collection = client['examotion']['test']

    def get_frequency(self):
        tabulations = {}

        for count in range(3):
            result = self.collection.count_documents({f'answers.{count}': answer_key[count]})
            tabulations[count+1] = result

        return tabulations

    def get_cnn(self):
        tabulations = {}

        for emotion in emotions:
            result = self.collection.count_documents({'cnns': emotion})
            tabulations[emotion] = result

        return tabulations

    def get_nlp(self):
        tabulations = {}

        for emotion in emotions:
            result = self.collection.count_documents({'nlps': emotion})
            tabulations[emotion] = result

        return tabulations

    def get_users(self):
        result = list(self.collection.find({}))

        return result
