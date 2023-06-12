'''
This will include all the authentication routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
# Request is used to get POST data
# Session is used to handle session database_name
# Redirect is used to redirect pages
# Url_for is used to get teh url for a route
# Flash is used to flash success or error messages
from flask import Blueprint, render_template, request, flash, session
# Import database handler functions
from .db_main import *
# Import connection variables
from .connections import *
# Import shopping cart functions
from .cart import *

female_items = Blueprint('female_items',__name__)


# Create routes
@female_items.route('/women_clothing', methods=['POST', 'GET'])
def women_clothing():
  '''
  Create a route for the women_clothing page

  Functionality:
  add item to cart
  
  Return:
    Product list template with Female sections that are dynamically added based on their inputs
  '''
  # get all female clothing products
  products1 = filter_by_category("Female clothing", "Shirt")
  products2 = filter_by_category("Female clothing", "Sweater")
  products3 = filter_by_category("Female clothing", "Pants")
  products4 = filter_by_category("Female clothing", "Skirt")
  products5 = filter_by_category("Female clothing", "Jersey")
  products6 = filter_by_category("Female clothing", "Jacket")
  # get all female accessory products
  products7 = filter_by_category("Female accessory", "Bag")
  products8 = filter_by_category("Female accessory", "Jewelry")
  products9 = filter_by_category("Female accessory", "Watch")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="All Female items", 
                         heading1="Shirts", 
                         products1=products1,
                         heading2="Sweaters", 
                         products2=products2,
                         heading3="Pants", 
                         products3=products3,
                         heading4="Skirts", 
                         products4=products4,
                         heading5="Jerseys", 
                         products5=products5,
                         heading6="Jackets", 
                         products6=products6,)
      
  return render_template("product_list.html", 
                         tab_title="All Female items", 
                         heading1="Shirts", 
                         products1=products1,
                         heading2="Sweaters", 
                         products2=products2,
                         heading3="Pants", 
                         products3=products3,
                         heading4="Skirts", 
                         products4=products4,
                         heading5="Jerseys", 
                         products5=products5,
                         heading6="Jackets", 
                         products6=products6,)

@female_items.route('/women_shirts', methods=['POST', 'GET'])
def women_shirts():
  '''
  Create a route for the women_shirts page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Female clothing", "Shirt")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Shirts", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Shirts", 
                         products1=products1,)

@female_items.route('/women_sweaters', methods=['POST', 'GET'])
def women_sweaters():
  '''
  Create a route for the women_sweaters page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Female clothing", "Sweater")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Sweaters", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Sweaters", 
                         products1=products1,)

@female_items.route('/women_jerseys', methods=['POST', 'GET'])
def women_jerseys():
  '''
  Create a route for the women_jerseys page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Female clothing", "Jersey")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Jerseys", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Jerseys", 
                         products1=products1,)

@female_items.route('/women_jackets', methods=['POST', 'GET'])
def women_jackets():
  '''
  Create a route for the women_jackets page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Female clothing", "Jacket")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Jackets", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Jackets", 
                         products1=products1,)

@female_items.route('/women_pants', methods=['POST', 'GET'])
def women_pants():
  '''
  Create a route for the women_pants page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Female clothing", "Pants")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Pants", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Pants", 
                         products1=products1,)

@female_items.route('/women_skirts', methods=['POST', 'GET'])
def women_skirts():
  '''
  Create a route for the women_skirts page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female clothing
  '''

  # get all male shirt products
  products1 = filter_by_category("Female clothing", "Skirt")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Skirts", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Skirts", 
                         products1=products1,)

@female_items.route('/women_bags', methods=['POST', 'GET'])
def women_bags():
  '''
  Create a route for the women_bags page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female accessory
  '''

  # get all male shirt products
  products1 = filter_by_category("Female accessory", "Bag")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Bags", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Bags", 
                         products1=products1,)

@female_items.route('/women_watches', methods=['POST', 'GET'])
def women_watches():
  '''
  Create a route for the women_watches page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female accessory
  '''

  # get all male shirt products
  products1 = filter_by_category("Female accessory", "Watch")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Watches", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Watches", 
                         products1=products1,)

@female_items.route('/women_jewelry', methods=['POST', 'GET'])
def women_jewelry():
  '''
  Create a route for the women_jewelry page

  Functionality:
  add item to cart
 
  Return:
    Product list template with Female accessory
  '''

  # get all male shirt products
  products1 = filter_by_category("Female accessory", "Jewelry")

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleared!', category='success')
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
                         tab_title="Female Items", 
                         heading1="Jewelry", 
                         products1=products1,)
      
  return render_template("product_list.html", 
                         tab_title="Female Items", 
                         heading1="Jewelry", 
                         products1=products1,)