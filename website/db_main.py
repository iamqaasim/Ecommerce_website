'''
Main CRUD a functions related to the database
'''
# import db connection variables
from .connections import *
# Request is used to get POST data
from flask import render_template, request, session, flash

# HELPER FUNCTIONS --------------------------------------------------------------------

def post_request_handler(search, product, add_to_cart, clear_cart, remove_from_cart):
  '''
  handle all post requests

  Return:
    return search, product, add_to_cart result
    return 0 if request invalid
  '''
  if search != 0:
    return search
  elif product != 0:
    return product
  elif add_to_cart == 'add to cart':
    return add_to_cart
  elif add_to_cart == 'not add to cart':
    return add_to_cart
  elif clear_cart == 'clear cart':
    return clear_cart
  elif clear_cart == 'not clear cart':
    return clear_cart
  elif remove_from_cart == 'item removed from cart':
    return remove_from_cart
  elif remove_from_cart == 'item not in cart':
    return remove_from_cart
  elif remove_from_cart == 'item not removed from cart':
    return remove_from_cart
  else:
    print("Post request function error")
    return 0
  

def nav_search():
  '''
  nav bar search function

  Return:
    return template of all the products found
    return 0 if search is empty
  '''
  try:
    search = request.form['nav_search']
    # check if search bar is empty
    if search != "":
      products1 = collection_1.find({"product_name": search})
      count = collection_1.count_documents({"product_name": search})
      return render_template("product_list.html", 
                             tab_title="Searched..", 
                             heading1=f"Items found: {count}",
                             products1=products1,)
    else:
      return 0
  except:
    return 0

def details_page():
  '''
  check if detail_button was clicked 

  Return:
    return template of edtails of the product
    return 0 if button not clicked
  '''
  try:
    product_ID = request.form['product']
    product = get_item(product_ID)
    # check if the details button was clicked
    if product:
      return render_template("product_details.html", 
                             product=product)
    else:
      return 0
  except:
    return 0


# ADD ITEM ----------------------------------------------------------------------------

def add_item(collection_name: str, doc: dict) -> bool:
  '''
  add new item to the database collection
  
  Args:
    collection_name (str): collection you want to use
    doc (dict): document you are adding

  Return:
    True - if item was successfully added
    False - otherwise
  '''
  try:
    insert_doc = collection_name.insert_one(doc)
    doc_id = insert_doc.inserted_id
    return doc_id
  except Exception:
    print('Could not add item to database')


# FIND ITEM ---------------------------------------------------------------------------

def get_item(product_ID: str):
  '''
  get the item based on the item ID 

  Args:
    product_ID: Stripe product ID
  
  Return:
    item object details
  '''
  try:
    item_found = collection_1.find_one({"stripe_product_id": product_ID})
    return item_found
  except Exception:
    print('No items in dataase')
    return None


def filter_by_category(category: str, sub_category: str):
  '''
  get the items based on the category and sub category

  Args:
    category (str): the cetegory of the item
    sub_category (str): the sub cetegory of the item
  
  Return:
    item ID
  '''
  try:
    all_items = collection_1.find({"category": [category, sub_category]})
    return list(all_items)
  except Exception:
    print('No items in dataase')
    return None


def find_all_items(collection_name: str):
  '''
  find all the items in the collection_name

  Args:
    collection_name (str): collection you want to use
  
  Return:
    list of all the items found
  '''
  try:
    all_items = list(collection_name.find())
    return all_items
  except Exception:
    print('No items in dataase')
    return None


def item_search(collection_name: str, index_name: str, index_path: str, query: str):
  '''
  strict search through collection_name

  This has to be set up in mongoDB atlas under the search tab

  Args:
    collection_name (str): collection you want to use
    index_name (str): name of the index you created on atlas
    index_path (str): the field your index is searching through, defined in atlas
    query (str): the 'search' you will submit

  Return 
    list of the items found
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


def total_item_count(collection_name: str):
  '''
  count the total amount of elements in the collection specified

  Args:
    collection_name (str): the database collection we want to count
  
  Return:
    total items in collection
  '''
  try:
    count = collection_name.count_documents({})
    return count
  except Exception:
    print('Could not count collection')


# UPDATE ITEM ------------------------------------------------------------------------

def update_item_data(collection_name: str, item: str, item_name: str, doc: dict) -> bool:
  '''
  update item info

  Args:
    collection_name (str): collection you want to use
    item (str): the cetegory of the item
    item_name (str): name of the item
    doc (dict): doc with updated details

  Return:
    True - if item was successfully updated
    False - otherwise 
  '''
  item_id = get_item_id(collection_name, item, item_name)
  _id = ObjectId(item_id)
  updates = {
    "$set": doc
  }
  collection_name.update_one({"_id": _id}, updates)
  return _id


# DELETE ITEM -------------------------------------------------------------------------

def remove_item(collection_name: str, item: str, item_name: str) -> bool:
  '''
  delete a item

  Args:
    collection_name (str): collection you want to use
    item (str): the cetegory of the item
    item_name (str): name of the item

  Return:
    True - if item was successfully deleted
    False - otherwise
  '''
  item_id = get_item_id(collection_name, item, item_name)
  _id = ObjectId(item_id)
  collection_name.delete_one({"_id": _id})
  return _id
