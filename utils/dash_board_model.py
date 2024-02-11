import tempfile
import pathlib
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from statics import static
from tempfile import TemporaryFile

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
        # Go back to the beginning and read data from file
        temp = ''
        for file in os.listdir(os.getcwd() + "\\myDir"):
            temp = pathlib.Path(os.path.join(os.getcwd() + "\\myDir", file)).suffix
            temp = temp.replace('.', '')

        self.admin = temp

    def get_frequency(self):
        # self.admin = "admin"
        tabulations = {}
        for count in range(3):
            result = self.collection.count_documents({'from': self.admin, f'answers.{count}': answer_key[count]})
            tabulations[count+1] = result

        return tabulations

    def get_cnn(self):
        tabulations = {}

        for emotion in emotions:
            result = self.collection.count_documents({'from': self.admin, 'cnns': emotion})
            tabulations[emotion] = result

        return tabulations

    def get_nlp(self):
        tabulations = {}

        for emotion in emotions:
            result = self.collection.count_documents({'from': self.admin, 'nlps': emotion})
            tabulations[emotion] = result

        return tabulations

    def get_users(self):
        result = list(self.collection.find({'from': self.admin}))
        print(self.admin)
        return result
