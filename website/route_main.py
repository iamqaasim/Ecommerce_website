'''
This will include all the authentication routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
# Request is used to get POST data
from flask import Blueprint, render_template, request, flash
# Import database handler functions
from .db_main import *
# Import connection variables
from .connections import *

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


@views.route('/about_us')
def about_us():
  '''
  Create a route for the about_us page

  Return:
    about us page
  '''
  return render_template("about_us.html")
