'''
Used to include all extention imports for the app
- database connection
- payment connection
- authentication connection
'''
# DATABASE CONNECTIONS --------------------------------------------------------------------------

# Connect MongoDB (quick start modules)
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# access environment variables
import os
# working with MongoDB's ObjectIDs.
from bson.objectid import ObjectId
# Allow payments
import stripe

# Create a new client and connect to the server
uri = os.environ['MONGO_URI'] # store connection string into environment varibale MONGO_URI
client = MongoClient(uri, server_api=ServerApi('1'))

# Define database
database_name = "store"
db = client[database_name]

# Define database collections
collection_name_1 = "products"
collection_name_2 = "users"
collection_name_3 = "insert_name_of_collection"
collection_name_4 = "insert_name_of_collection"
collection_name_5 = "insert_name_of_collection"

collection_1 = db[collection_name_1]
collection_2 = db[collection_name_2]
collection_3 = db[collection_name_3]
collection_4 = db[collection_name_4]
collection_5 = db[collection_name_5]

# PAYMENT CONNECTIONS ---------------------------------------------------------------------------

# Connect stripe API 
stripe.api_key = os.environ['STRIPE_SCT']

