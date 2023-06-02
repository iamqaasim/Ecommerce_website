'''
All CRUD and testing functions related to the database

The variables can be changed according to your requirments
'''
# import db connection variables
from .extensions import *


# create functions ------------------------------------------------------------------------------------------------------

def add_item(collection_name, doc: dict):
  '''
  add new item to the database collection

  collection_name: collection you want to use
  doc: document you are adding

  return the ID of the inserted document
  '''
  try:
    insert_doc = collection_name.insert_one(doc)
    doc_id = insert_doc.inserted_id
    return doc_id
  except Exception:
    print('Could not add item to database')


# read / find functions -------------------------------------------------------------------------------------------------

def get_item_id(collection_name, item: str, item_name: str):
  '''
  get the item ID based on the item and item name (this should be chnaged based on your requirements) 

  collection_name: collection you want to use

  
  item:
  item_name:
  
  return item id
  '''
  try:
    item_found = collection_name.find_one({"item": item, "item_name": item_name})
    item_id = item_found['_id']
    return item_id
  except Exception:
    print('No items in dataase')
    return None


def find_all_items(collection_name):
  '''
  find all the items in the collection_name

  returns a list of all the items found
  '''
  try:
    all_items = list(collection_name.find())
    return all_items
  except Exception:
    print('No items in dataase')
    return None


def item_search(collection_name, index_name: str, index_path: str, query: str):
  '''
  strict search through collection_name

  This has to be set up in mongoDB atlas under the search tab

  return a list of the products
  '''
  
  try:
    result = collection_name.aggregate([
    {
      "$search":{
        "index": index_name,
        "text": {
          "query": query,
          "path": index_path
          }
        }
      }
    ])
    return list(result)
  except Exception:
    print('Could not find item in database')
  

# update functions ------------------------------------------------------------------------------------------------------

def update_item_data(collection_name, item: str, item_name: str, doc: dict):
  '''
  update item info

  return ID of updated item 
  '''
  item_id = get_item_id(collection_name, item, item_name)
  _id = ObjectId(item_id)
  updates = {
    "$set": doc
  }
  collection_name.update_one({"_id": _id}, updates)
  return _id


# delete functions ------------------------------------------------------------------------------------------------------

def remove_item( collection_name, item: str, item_name: str):
  '''
  delete a item
  
  return deleted item ID
  '''
  item_id = get_item_id(collection_name, item, item_name)
  _id = ObjectId(item_id)
  collection_name.delete_one({"_id": _id})
  return _id


# other functions -------------------------------------------------------------------------------------------------------

def total_item_count(collection_name):
  '''
  count the total amount of elements in the collection specified

  collection_name: the database collection we want to count
  
  return the total items in collection
  '''
  try:
    count = collection_name.count_documents({})
    return count
  except Exception:
    print('Could not count collection')


# Database connection test ---------------------------------------------------------------------------------------------

def testing_db_conenction():
  '''
  Send a ping to confirm a successful connection
  '''
  try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
    print(e)