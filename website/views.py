'''
This will include all the routes used for the site
'''

# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, jsonify
# Import database handler functions
from .database import *

views = Blueprint('views',__name__)


# Create routes
@views.route('/home')
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

AUTHENTICATION: (create and register blueprint)
route for signing up
route for signing in / logging in
route for signing out / logging out

PAYMENT:
route for payment(cart)
'''


# testing route ----------------------------------------------------------------------------------------------
@views.route('/')
def testing():
  '''
  Create a route for testing
  '''
  doc = {
    "user": "person1",
    "name": "shirt",
    "price": 100,
    "category": "Men"
  }
  doc1 = {
    "user": "updated user name",
    "name": "shirt",
    "category": "men"
  }
  # add a product, doc
  add = add_product(doc)

  # get the ID of the product based on the user name and product name
  get_id = get_product_id('person1', 'shirt')

  # my find function
  all_products = find_all_products()

  # mongodb search engin
  searched_products = product_search('shirt')

  # update product, using the requirmtns for get_product_id to identify the correct product and doc1 to update the various fields
  updates = update_product_data('person1', 'shirt', doc1)

  #delete a product, using the requirmtns for get_product_id to identify the correct product and deleting it using the product_id
  removed_product = remove_product('updated user name', 'shirt')

  # count the items in the products collection
  count = total_item_count(products)
  
  return render_template("testing_template.html", 
                         count = count, 
                         add = add, 
                         all_products = all_products, 
                         searched_products = searched_products, 
                         updates = updates, 
                         removed_product = removed_product, 
                         get_id = get_id)