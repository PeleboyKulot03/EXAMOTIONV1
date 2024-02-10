from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://juliusandrie28:r6vDShlcMCC1HaYT@testcluster.mgngbbc.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

collection = client['examotion']['test']

# find documents
result = collection.count_documents({'answers.0': "A"})
# print results
print("Document found:\n", result)
