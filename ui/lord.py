from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

test = [[2, 1, 4, 3, 1, 1, 1, 1, "I feel nervous becasue I didn't study the module"],
        [5, 2, 1, 1, 2, 3, 3, 1,  "None"],
        [2, 1, 1, 2, 1, 3, 1, 2, "Im feel happy"],
        [1, 2, 2, 1, 2, 1, 3, 2, "I feel sad"],
        [1, 2, 3, 1, 2, 5, 1, 3, "Im nervous"],
        [3, 1, 1, 2, 1, 3, 1, 4, "Happy"],
        [2, 3, 2, 3, 3, 3, 1, 3, "Not so good"],
        [5, 2, 3, 1, 3, 3, 4, 3, "Okay lang po"],
        [1, 1, 3, 3, 4, 5, 4, 3, "Is good but is nervous"],
        [3, 3, 2, 1, 2, 3, 3, 3, "im fine"],
        [3, 3, 3, 3, 2, 3, 4, 3, "I feel confident"],
        [1, 1, 3, 4, 3, 4, 3, 3, "Im shy"],
        [3, 3, 3, 5, 4, 3, 3, 3, "Nervous"],
        [2, 1, 4, 4, 3, 4, 3, 3, "just okay"],
        [3, 3, 3, 4, 3, 4, 3, 4, "ok"]
        ]

load_dotenv()
cluster = os.getenv("CLUSTER")
uri = cluster
client = MongoClient(uri)
collection = client['examotion']['students']

names = ['Christine Joy C. Corbita', 'cassandra mae L. cuartero', 'Junsay Cyrus G', 'nathaniel', 'john kevin',
         'Cris lenard L. Rodanilla', 'Bryan', 'Ryan Marc C. Dante', 'Dela Cruz John Bryan S.', 'rodz',
         'Eliah kim Sabaybay', 'IVAN ', 'Paolo Pagsuyuin', 'mark angelo ', 'anthony']

