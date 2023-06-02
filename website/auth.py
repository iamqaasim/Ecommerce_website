'''
This will include all the authentication routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, request, session, redirect
# Import database CRUD functions
from .database import *
# import db connection variables
from .extensions import *

# initiate blueprint called "auth"
auth = Blueprint('auth',__name__)


'''
ROUTES TO BE ADDED:

AUTHENTICATION: 
route for signing up
route for signing in / logging in
route for signing out / logging out

'''


# Create routes
@auth.route('/signup', methods=['POST', 'GET'])
def signup():
  '''
  Create a route for the signup page 
  '''
  if request.method == 'POST':
    print('post method')
    user_exist = collection_3.find_one({'name': request.form['username']})
    
    if user_exist is None:
      print('user exit')
      hashpassword = _hash_password(request.form['password'])
      
      user_form = {
        'name': request.form['username'],
        'password': hashpassword
      }
      
      add_item(collection_3, user_form)
      print('user added to database')
      
      session['username'] = request.form['username']
      
      return redirect(url_for('home'))
    return 'username exist!'

  return render_template("signup.html")


@auth.route('/login')
def login():
  '''
  Create a route for the login page 
  '''
  return render_template("login.html")


@auth.route('/logout')
def logout():
  '''
  Create a route for logging out 
  '''
  return render_template("login.html")