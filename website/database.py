'''
All CRUD and testing functions related to the database
'''

# import db connection variables
from .extensions import *


# create functions ------------------------------------------------------------------------------------------------------

def add_product(doc: dict):
  '''
  add new products to the database

  return the ID of the inserted document
  '''
  try:
    insert_doc = products.insert_one(doc)
    doc_id = insert_doc.inserted_id
    return doc_id
  except Exception:
    print('Could not add product to database')

# read / find functions -------------------------------------------------------------------------------------------------

def get_product_id(user_name: str, product_name: str):
  '''
  get the product id based on the product name 

  product_name: name of the product
  
  return product id
  '''
  product = products.find_one({"user": user_name, "name": product_name})
  product_id = product['_id']
  return product_id


def find_all_products():
  '''
  find all the products in the database

  returns a list of all the products
  '''
  try:
    all_products = list(products.find())
    return all_products
  except Exception:
    print('No products in dataase')

def product_search(query: str):
  '''
  strict search through products collection

  query: users searched text

  return a list of the products
  '''
  try:
    result = products.aggregate([
    {
      "$search":{
        "index": "product_search",
        "text": {
          "query": query,
          "path": "name"
          }
        }
      }
    ])
    return list(result)
  except Exception:
    print('Could not find product in database')
  

# update functions ------------------------------------------------------------------------------------------------------

def update_product_data(user_name: str, product_name: str, doc: dict):
  '''
  update product info

  user_name: name of the user who wants to delete the product
  product_name: nam eof the product user wants to delete

  return ID of updated product 
  '''
  product_id = get_product_id(user_name, product_name)
  _id = ObjectId(product_id)
  updates = {
    "$set": doc
  }
  products.update_one({"_id": _id}, updates)
  return _id

# delete functions ------------------------------------------------------------------------------------------------------

def remove_product(user_name: str, product_name: str):
  '''
  delete a product

  user_name: name of the user who wants to delete the product
  product_name: nam eof the product user wants to delete
  
  return deleted product ID
  '''
  product_id = get_product_id(user_name, product_name)
  _id = ObjectId(product_id)
  products.delete_one({"_id": _id})
  return _id

# other functions -------------------------------------------------------------------------------------------------------

def total_item_count(collection):
  '''
  count the total amount of elements in the collection specified

  collection: the database collection we want to count
  
  return the total items in collection
  '''
  try:
    count = collection.count_documents({})
    return count
  except Exception:
    print('Could not count collection')


# Database function testing ---------------------------------------------------------------------------------------------

def testing_db_conenction():
  '''
  Send a ping to confirm a successful connection
  '''
  try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
    print(e)