'''
This will include all the routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, jsonify
# Import database handler functions
from .database import *
# Import connection variables
from .extensions import *

views = Blueprint('views',__name__)


# Create routes
@views.route('/')
def home():
  '''
  Create a route for the Home page 
  '''
  return render_template("home.html")


'''
ROUTES TO BE ADDED:

VIEWS:
route for men clothing
  -sub routes for: shirts, sweaters, pants, jerseys, jackets, shoes

route for women clothing
  -sub routes for: skirts, shirts, sweaters, pants, jerseys, jackets, shoes

route for accessories
  -sub route for men
    -sub sub routes: watches, jewelry, bags
  -sub route for women
    -sub sub routes: watches, jewelry, bags
'''

@views.route('/men_clothing')
def men_clothing():
  '''
  Create a route for the men_clothing page 
  '''
  return render_template("men_clothing.html")

@views.route('/women_clothing')
def women_clothing():
  '''
  Create a route for the women_clothing page 
  '''
  return render_template("women_clothing.html")

@views.route('/accessories')
def accessories():
  '''
  Create a route for the accessories page 
  '''
  return render_template("accessories.html")

@views.route('/contact_us')
def contact_us():
  '''
  Create a route for the contact_us page 
  '''
  return render_template("contact_us.html")

@views.route('/about_us')
def about_us():
  '''
  Create a route for the about_us page 
  '''
  return render_template("about_us.html")

# testing route --------------------------------------------------------------------------------

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


@views.route('/testing')
def testing():
  '''
  Create a route for testing
  '''
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
  
  return render_template("testing_template.html", 
                         count_items = count_items, 
                         add_item = add_items, 
                         all_items = all_items, 
                         searched_items = searched_items, 
                         update_item = update_item, 
                         removed_item = removed_item, 
                         get_id = get_id)