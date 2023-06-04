'''
This will include all the testing routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# Import database related functions
from .db_main import *
from .db_stripe import *
# Import connection variables
from .connections import *

test = Blueprint('test',__name__)

# testing docs
item_doc = {
  "image": "some image",
  "item": "item",
  "item_name": "item name",
  "item_category": "item category",
}
new_item_doc = {
  "item": "updated item",
  "item_name": "new name",
}
user = {
  "username": "user name",
  "firstname": "name of user",
  "surname": "surname of user",
  "password": "password",
  "gender": "male or female",
  "email": "email",
  "data_of_birth": ["day", "month", "year"],
  "address": "address",
  "last_login": ["day", "month", "year"],
  "account_creation": ["day", "month", "year"]
}
product = {
  "image": "some image",
  "name": "product name",
  "description": "product description",
  "price": 100,
  "category": "accessry or clothing",
  "gender": "male or female",
  "stock_amount": 10,
  "brand": "some brand",
  "size": "small, medium or large"
}

@test.route('/database')
def database():
  '''
  Create a route for testing
  '''
  item_doc = {
    "item": "item",
    "item_name": "item name",
    "item_category": "item category"
  }
  new_item_doc = {
    "item": "updated item",
    "item_name": "new name",
  }
  # add a item
  add_items = add_item(collection_1, item_doc)

  # get the ID of the item based on the user name and product name
  get_id = get_item_id(collection_1, 'item', 'item name')

  # list all item in collection
  all_items = find_all_items(collection_1)

  # mongodb search engine 
  '''
  This will only work if you configured the search index on atlas
  '''
  index_name = "product_search" # name of the search index
  index_path = "name" # which field are searching through
  query = "item" # what are you searching
  searched_items = item_search(collection_1, index_name, index_path, query)

  # update item fields
  update_item = update_item_data(collection_1, 'item', 'item name', new_item_doc)

  # delete an item
  removed_item = remove_item(collection_1, 'updated item', 'new name')

  # count the items in the products collection
  count_items = total_item_count(collection_1)
  
  return render_template("testing_db.html", 
                         count_items = count_items, 
                         add_item = add_items, 
                         all_items = all_items, 
                         searched_items = searched_items, 
                         update_item = update_item, 
                         removed_item = removed_item, 
                         get_id = get_id)


@test.route('/authenticate', methods=['POST', 'GET'])
def authenticate():
  '''
  Create a route for testing
  '''
  if request.method == 'POST':
    # request form data
    request_name = request.form['name']
    request_user = request.form['username']
    request_email = request.form['email']
    request_password = request.form['password']
  
    hash_passwords = hash_password(request_password)
    print(hash_passwords)
    
    registered_users = register_user(request_name, request_user, request_email, request_password)
    print(registered_users)
    
    valid_login = validate_login(request_user, request_password) 
    print(valid_login)
    
    deleted_user = remove_user("user")
    print(deleted_user)
    
    return render_template("testing_auth.html", 
                           method = 'POST',
                           hash_passwords = hash_passwords, 
                           registered_users = registered_users, 
                           valid_login = valid_login, 
                           request_name = request_name, 
                           request_user = request_user, 
                           request_email = request_email, 
                           request_password = request_password,
                           deleted_user = deleted_user)
  
  return render_template("testing_auth.html", method='GET')

@test.route('/payments')
def payments():
  '''
  Create a route for testing
  '''
  add_stripe_product('product_name')
  return 'test payment'
