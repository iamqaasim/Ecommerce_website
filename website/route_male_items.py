'''
This will include all the authentication routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
# Request is used to get POST data
from flask import Blueprint, render_template, request, flash, session
# Import database handler functions
from .db_main import *
# Import connection variables
from .connections import *
# Import shopping cart functions
from .cart import *

male_items = Blueprint('male_items',__name__)


# Create routes
@male_items.route('/men_clothing', methods=['POST', 'GET'])
def men_clothing():
  '''
  Create a route for the men_clothing page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Male sections that are dynamically added based on their inputs
  '''

  # get all male clothing products
  products1 = filter_by_category("Male clothing", "Shirt")
  products2 = filter_by_category("Male clothing", "Sweater")
  products3 = filter_by_category("Male clothing", "Pants")
  products4 = filter_by_category("Male clothing", "Jersey")
  products5 = filter_by_category("Male clothing", "Jacket")
  # get all male accessory products
  products6 = filter_by_category("Male accessory", "Bag")
  products7 = filter_by_category("Male accessory", "Watch")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("product_list.html", 
                         tab_title="All Male items", 
                         heading1="Shirts", 
                         products1=products1,
                         heading2="Sweaters", 
                         products2=products2,
                         heading3="Pants", 
                         products3=products3,
                         heading4="Jerseys", 
                         products4=products4,
                         heading5="Jackets", 
                         products5=products5,)
      
  return render_template("product_list.html", 
                         tab_title="All Male items", 
                         heading1="Shirts", 
                         products1=products1,
                         heading2="Sweaters", 
                         products2=products2,
                         heading3="Pants", 
                         products3=products3,
                         heading4="Jerseys", 
                         products4=products4,
                         heading5="Jackets", 
                         products5=products5,)

@male_items.route('/men_shirts', methods=['POST', 'GET'])
def men_shirts():
  '''
  Create a route for the men_shirts page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Male clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Male clothing", "Shirt")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Shirts", 
                         products1=products1,)
  
  return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Shirts", 
                         products1=products1,)

@male_items.route('/men_sweaters', methods=['POST', 'GET'])
def men_sweaters():
  '''
  Create a route for the men_sweaters page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Male clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Male clothing", "Sweater")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Sweaters", 
                         products1=products1,)
  
  return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Sweaters", 
                         products1=products1,)

@male_items.route('/men_jerseys', methods=['POST', 'GET'])
def men_jerseys():
  '''
  Create a route for the men_jerseys page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Male clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Male clothing", "Jersey")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Jerseys", 
                         products1=products1,)
  
  return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Jerseys", 
                         products1=products1,)

@male_items.route('/men_jackets', methods=['POST', 'GET'])
def men_jackets():
  '''
  Create a route for the men_jackets page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Male clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Male clothing", "Jacket")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Jackets", 
                         products1=products1,)
  
  return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Jackets", 
                         products1=products1,)

@male_items.route('/men_pants', methods=['POST', 'GET'])
def men_pants():
  '''
  Create a route for the men_pants page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Male clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Male clothing", "Pants")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Pants", 
                         products1=products1,)
  
  return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Pants", 
                         products1=products1,)

@male_items.route('/men_bags', methods=['POST', 'GET'])
def men_bags():
  '''
  Create a route for the men_bags page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Male accessory
  '''

  # get all male shirt products
  products1 = filter_by_category("Male accessory", "Bag")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Bags", 
                         products1=products1,)
  
  return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Bags", 
                         products1=products1,)

@male_items.route('/men_watches', methods=['POST', 'GET'])
def men_watches():
  '''
  Create a route for the men_watches page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Male accessory
  '''

  # get all male shirt products
  products1 = filter_by_category("Male accessory", "Watch")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Watches", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Male Items", 
                         heading1="Watches", 
                         products1=products1,)