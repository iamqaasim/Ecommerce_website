'''
CRUD functions related to stripe API

Stripe API was used to fetch the item data
'''
# import db connection variables
from .connections import *
# Import database handler functions
from .db_main import *



# ADD PRODUCT -------------------------------------------------------------------------

def add_stripe_product(product_key: str, category: str, sub_category: str) -> int:
  '''
  add stripe product to MongoDB

  Args:
    product_key: Stripe product key
    category: male or female categories (clothing or accessory)
    sub_category: clothing or accessory sub catetories (sweater, shirt, pants, etc..)

  Return:
    0 if item already found in MongoDB
    1 if item added to MongoDB
    2 if product key not found in Stripe
  '''
  
  try:
    # fetch stripe data
    product_data = stripe.Product.retrieve(product_key)
    
    if product_data != None:
      # fetch stripe price data
      price_data = stripe.Price.retrieve(product_data['default_price'])
      if product_data['images'] == []:
        image = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_38GaBgnp-f3c5IXYIUXFacnep2C53O71N9kWeQq5ZlkVDXq5hSbUefj8ZM_hSslCl8k&usqp=CAU']
      else: 
        image = product_data['images']

      # document for MongoDB
      doc = {
        "stripe_product_id": product_data['id'],
        "username": "username",
        "product_name": product_data['name'],
        "price_data": {
          "stripe_price_id": price_data['id'],
          "price": price_data['unit_amount']
        },
        "product_description": product_data['description'],
        "image": image,
        "category": [category, sub_category]
      }
      
      # check if item exist in MongoDB
      item_found = collection_1.find_one({"stripe_product_id": product_data['id']})
  
      if item_found:
        return 0
      else:
        # add document to mongoDB
        add_item(collection_1, doc)
        return 1
    else:
      return 2
  except Exception as e:
    return e


# FIND PRODUCT -------------------------------------------------------------------------

def find_stripe_product(product_key: str) -> int:
  '''
  find stripe product in MongoDB

  Args:
    product_key: Stripe product key
    
  Return:
    0 if item in MongoDB
    1 if item not found in MongoDB
    2 if product key not found in Stripe
  '''
  
  try:
    # fetch stripe data
    product_data = stripe.Product.retrieve(product_key)
    
    if product_data != None:
      # check if item exist in MongoDB
      item_found = collection_1.find_one({"stripe_product_id": product_data['id']})
  
      if item_found:
        return 0
      else:
        return 1
    else:
      return 2
  except Exception as e:
    return e

# UPDATE PRODUCT -----------------------------------------------------------------------

def update_stripe_product(product_key: str, category: str, sub_category: str) -> int:
  '''
  update stripe product in MongoDB

  Args:
    product_key: Stripe product key
    category: male or female categories (clothing or accessory)
    sub_category: clothing or accessory sub catetories (sweater, shirt, pants, etc..)

  Return:
    0 if item was updated
    1 if item not found in MongoDB
    2 if product key not found in Stripe
  '''
  
  try:
    # fetch stripe data
    product_data = stripe.Product.retrieve(product_key)
    
    if product_data != None:
      # fetch stripe price data
      price_data = stripe.Price.retrieve(product_data['default_price'])
    
      # document for MongoDB
      doc = {
        "stripe_product_id": product_data['id'],
        "username": "username",
        "product_name": product_data['name'],
        "price_data": {
          "stripe_price_id": price_data['id'],
          "price": price_data['unit_amount']
        },
        "product_description": product_data['description'],
        "category": product_data['unit_label'],
        "image": product_data['images'],
        "category": [category, sub_category]
      }

      updates = {
        "$set": doc
      } 
      
      # check if item exist in MongoDB
      item_found = collection_1.find_one({"stripe_product_id": product_data['id']})
  
      if item_found:
        # add updated document to mongoDB
        collection_1.update_one({"stripe_product_id": product_data['id']},updates)
        return 0
      else:
        return 1
    else:
      return 2
  except Exception as e:
    return e

# DELETE PRODUCT -----------------------------------------------------------------------

def remove_stripe_product(product_key: str) -> bool:
  '''
  delete stripe product from MongoDB

  Return:
    0 if item was removed
    1 if item not found in MongoDB
    2 if product key not found in Stripe
  '''
  
  try:
    # fetch stripe data
    product_data = stripe.Product.retrieve(product_key)
    
    if product_data != None:
      # check if item exist in MongoDB
      item_found = collection_1.find_one({"stripe_product_id": product_data['id']})
  
      if item_found:
        # remove document from mongoDB
        collection_1.delete_one({"stripe_product_id": product_data['id']})
        return 0
      else:
        return 1
    else:
      return 2
  except Exception as e:
    return e
