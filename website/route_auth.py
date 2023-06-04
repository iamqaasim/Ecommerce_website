'''
This will include all the main routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# Log manager
from flask_login import login_user, logout_user, login_required , current_user
# import main CRUD functions
from.db_main import *
# authentication functions
from .db_auth import *
# import db connection variables
from .connections import *


# initiate blueprint called "auth"
auth = Blueprint('auth',__name__)


# Create routes
@auth.route('/signup', methods=['POST', 'GET'])
def signup():
  '''
  Create a route for the signup page

  GET method:
    display sign up page

  POST method:
    send necessary fields needed to sign up (name, username, email, password)

  Return:
    valid = 0 if user not in database
      sign up new user
      redirects to home page
    valid = 1 if user is in database but incorrect password
      flash incorrect password
    valid = 2 if correct user an correct password
      login user
      redirects to home page
  '''
  
  if request.method == 'POST':
    # request form data
    request_name = request.form['name']
    request_user = request.form['username']
    request_email = request.form['email']
    request_password = request.form['password']

    valid = validate_login(request_user, request_password)

    if valid == 0:
      register_user(request_name, request_user, request_email, request_password)
      flash('signed up', category='success')
      return redirect(url_for('views.home'))
    elif valid == 1:
      flash('user exist, password invalid', category='error')
    elif valid == 2:
      flash('logged in', category='success')
      return redirect(url_for('views.home'))
    else:
      return valid
    # register_user(request_name, request_user, request_email, request_password)

  return render_template("signup.html")


@auth.route('/login', methods=['POST', 'GET'])
def login():
  '''
  Create a route for the login page

  GET method:
    display login page

  POST method:
    send necessary fields needed to login (username & password)

  Return:
    valid = 0 if user not in database
      flash incorrect user
    valid = 1 if user is in database but incorrect password
      flash incorrect password
    valid = 2 if correct user an correct password
      login user
      redirects to home page
  '''
  
  if request.method == 'POST':
    # request form data
    request_user = request.form['username']
    request_password = request.form['password']
    
    valid = validate_login(request_user, request_password)

    if valid == 0:
      flash('username doesnt exist', category='error')
    elif valid == 1:
      flash('invalid password', category='error')
    elif valid == 2:
      flash('logged in', category='success')
      return redirect(url_for('views.home'))
    else:
      return valid
  return render_template("login.html")

@auth.route('/logout')
def logout():
  '''
  Create a route for logging out

  Return:
    flash logout message
    redirect to login page
  '''
  
  flash('logged out', category='error')
  return redirect(url_for('auth.login'))