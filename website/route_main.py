'''
This will include all the authentication routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, jsonify, request
from flask_login import login_user, logout_user, login_required , current_user
# Import database handler functions
from .db_main import *
# Import connection variables
from .connections import *
from forms import NewProduct, ContactUs

views = Blueprint('views',__name__)


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

# Create routes
@views.route('/')
def home():
  '''
  Create a route for the Home page

  Functionality:
    view top purchased products
  
  Return:
    home page
  '''
  return render_template("home.html")


@views.route('/men_clothing')
def men_clothing():
  '''
  Create a route for the men_clothing page

  Functionality:
  add item to cart
 
  Return:
    Display the list of male clothing ONLY
  '''
  return render_template("men_clothing.html")


@views.route('/women_clothing')
def women_clothing():
  '''
  Create a route for the women_clothing page

  Functionality:
  add item to cart
  
  Return:
    Display the list of female clothing ONLY
  '''
  return render_template("women_clothing.html")


@views.route('/accessories')
def accessories():
  '''
  Create a route for the accessories page

  Functionality:
  add item to cart
  
  Return:
    Display and list of male and female assesories
  '''
  return render_template("accessories.html")


@views.route('/contact_us')
def contact_us():
  '''
  Create a route for the contact_us page

  POST method:
    send a email directly to bsuiness email acount
  
  Return:
    contact page
  '''
  form = ContactUs()
  return render_template("contact_us.html", form=form)


@views.route('/about_us')
def about_us():
  '''
  Create a route for the about_us page

  Return:
    about us page
  '''
  return render_template("about_us.html")


@views.route('/new_product')
def new_product():
  '''
  Create a route for adding a new product to the db

  Return:
    new_product page
  '''
  form = NewProduct()
  return render_template("new_product.html", form=form)

