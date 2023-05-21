# Used to include all extention imports for the app

# Connect MongoDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

# Create a new client and connect to the server
uri = os.environ['MONGO_URI']
client = MongoClient(uri, server_api=ServerApi('1'))