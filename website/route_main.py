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
from flask import Blueprint, render_template, request, url_for, flash, session, redirect
# Import database handler functions
from .db_main import *
# Import connection variables
from .connections import *
# Import shopping cart functions
from .cart import *

views = Blueprint('views',__name__)


# Create routes
@views.route('/', methods=['POST', 'GET'])
def home():
  '''
  Create a route for the Home page

  Functionality:
    view top purchased products
  
  Return:
    Product list template with sections that are dynamically added based on their inputs
  '''
  
  if "user" not in session:
    flash(f'You need to login :)', category='error')
    return redirect(url_for('auth.login'))
  
  # Section 1 Male data
  heading1 = "Male clothing"
  products1 = find_all_items(collection_1)
  
  # Section 2 Female data
  heading2 = "Female clothing"
  products2 = find_all_items(collection_1)
  
  # Section 3 Accessory data
  heading3 = "Accessories"
  products3 = find_all_items(collection_1)

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
     return render_template("home.html", 
                         tab_title="All products", 
                         heading1=heading1, 
                         products1=products1, 
                         heading2=heading2, 
                         products2=products2,
                         heading3=heading3, 
                         products3=products3,)
  
    
  return render_template("home.html", 
                         tab_title="All products", 
                         heading1=heading1, 
                         products1=products1, 
                         heading2=heading2, 
                         products2=products2,
                         heading3=heading3, 
                         products3=products3,)


@views.route('/accessories', methods=['POST', 'GET'])
def accessories():
  '''
  Create a route for the accessories page

  Functionality:
  add item to cart
  
  Return:
    Product list template with Accessory sections that are dynamically added based on their inputs
  '''
  # get all jewlry
  products1 = filter_by_category("Female accessory", "Jewelry")
  # get all watches
  products2 = filter_by_category("Female accessory", "Watch")
  products3 = filter_by_category("Male accessory", "Watch")
  # get all bags
  products4 = filter_by_category("Female accessory", "Bag")
  products5 = filter_by_category("Male accessory", "Bag")

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
                         tab_title="All Accessory items", 
                         heading1="Jewelry", 
                         products1=products1,
                         section2="Watches",
                         heading2="Female watches", 
                         products2=products2,
                         heading3="Male watches", 
                         products3=products3,
                         section4="Bags", 
                         heading4="Female bags", 
                         products4=products4,
                         heading5="Male bags", 
                         products5=products5,)
      
  return render_template("product_list.html", 
                         tab_title="All Accessory items", 
                         heading1="Jewelry", 
                         products1=products1,
                         section2="Watches",
                         heading2="Female watches", 
                         products2=products2,
                         heading3="Male watches", 
                         products3=products3,
                         section4="Bags", 
                         heading4="Female bags", 
                         products4=products4,
                         heading5="Male bags", 
                         products5=products5,)


@views.route('/contact_us', methods=['POST', 'GET'])
def contact_us():
  '''
  Create a route for the contact_us page

  POST method:
    send a email directly to business email acount
  
  Return:
    contact page
  '''

  if request.method == 'POST':
    # request form data
    request_name = request.form['name']
    request_email = request.form['email']
    request_subject = request.form['subject']
    request_message = request.form['message']
    
    # set email fields
    email_reciever = request_email
    email_subject = f"{request_subject} - {request_name}"
    email_message = request_message
    
    # configure email feilds
    try:
      em['From'] = email_sender
      em['To'] = email_reciever
      em['Subject'] = email_subject
      em.set_content(f"{email_message}")
    except Exception:
      flash('Please fill all fields before submitting!', category='error')
      return render_template("contact_us.html")
      
    # send secure email
    try:
      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
        flash('Email sent!', category='success')
    except Exception:
      flash('There was an error!', category='error')
      flash('Please insert valid Email address!', category='error')
      return render_template("contact_us.html")
      
  return render_template("contact_us.html")


@views.route('/about_us', methods=['POST', 'GET'])
def about_us():
  '''
  Create a route for the about_us page

  Return:
    about us page
  '''
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
     return render_template("about_us.html")
  return render_template("about_us.html")


@views.route('/product_details', methods=['POST', 'GET'])
def product_details():
  '''
  Create a route for to display ALL products details

  Return:
    Product list template with sections that are dynamically added based on their inputs
  '''
  
  product_ID = 'prod_O3EfeAAcW6lqpg'
  product = get_item(product_ID)
  #print(product_details)

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
     return render_template("product_details.html", product=product)
      
  return render_template("product_details.html", product=product)

@views.route('/all_products', methods=['POST', 'GET'])
def all_products():
  '''
  Create a route for to display ALL products in the databsae

  Return:
    Product list template with sections that are dynamically added based on their inputs
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
  # get all male clothing products
  products10 = filter_by_category("Male clothing", "Shirt")
  products11 = filter_by_category("Male clothing", "Sweater")
  products12 = filter_by_category("Male clothing", "Pants")
  products13= filter_by_category("Male clothing", "Jersey")
  products14 = filter_by_category("Male clothing", "Jacket")
  # get all male accessory products
  products15 = filter_by_category("Male accessory", "Bag")
  products16 = filter_by_category("Male accessory", "Watch")

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
                         tab_title="All products",
                         section1="Shirts", 
                         heading1="Shirts (female)", products1=products1,
                         heading2="Shirts (male)", products2=products10,
                         section3="Sweaters",
                         heading3="Sweaters (female)", products3=products2,
                         heading4="Sweaters (male)", products4=products11,
                         section5="Jerseys",
                         heading5="Jerseys (female)", products5=products5,
                         heading6="Jerseys (male)", products6=products13,
                         section7="Jackets",
                         heading7="Jackets (female)", products7=products6,
                         heading8="Jackets (male)", products8=products14,
                         section9="Pants",
                         heading9="Pants (female)", products9=products3,
                         heading10="Pants (male)", products10=products12,
                         section11="Skirts",
                         heading11="Skirts (female)", products11=products4,
                         section12="Watches",
                         heading12="Watches (female)", products12=products9,
                         heading13="Watches (male)", products13=products16,
                         section14="Bags",
                         heading14="Bags (female)", products14=products7,
                         heading15="Bags (male)", products15=products15,
                         section16="Jewelry",
                         heading16="Jewelry (female)", products16=products8,)
      
  return render_template("product_list.html", 
                         tab_title="All products",
                         section1="Shirts", 
                         heading1="Shirts (female)", products1=products1,
                         heading2="Shirts (male)", products2=products10,
                         section3="Sweaters",
                         heading3="Sweaters (female)", products3=products2,
                         heading4="Sweaters (male)", products4=products11,
                         section5="Jerseys",
                         heading5="Jerseys (female)", products5=products5,
                         heading6="Jerseys (male)", products6=products13,
                         section7="Jackets",
                         heading7="Jackets (female)", products7=products6,
                         heading8="Jackets (male)", products8=products14,
                         section9="Pants",
                         heading9="Pants (female)", products9=products3,
                         heading10="Pants (male)", products10=products12,
                         section11="Skirts",
                         heading11="Skirts (female)", products11=products4,
                         section12="Watches",
                         heading12="Watches (female)", products12=products9,
                         heading13="Watches (male)", products13=products16,
                         section14="Bags",
                         heading14="Bags (female)", products14=products7,
                         heading15="Bags (male)", products15=products15,
                         section16="Jewelry",
                         heading16="Jewelry (female)", products16=products8,)