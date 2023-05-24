'''
Used to include all extention imports for the app
- database connection
- payment connection
- authentication connection
'''
# DATABASE CONNECTIONS -----------------------------------------------------------------------------

# Connect MongoDB (quick start modules)
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# access environment variables
import os
# working with MongoDB's ObjectIDs.
from bson.objectid import ObjectId

# Create a new client and connect to the server
uri = os.environ['MONGO_URI']
client = MongoClient(uri, server_api=ServerApi('1'))

# Define database
db = client["store"]

# Define database collections
products = db["products"]
users = db["users"]

# PAYMENT CONNECTIONS -----------------------------------------------------------------------------