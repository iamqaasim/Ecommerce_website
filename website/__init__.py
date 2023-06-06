'''
Converts the website folder into a python package so that we can export data between files
'''
# Flask is used to create a quick website backend 
from flask import Flask
# timer
from datetime import timedelta

# Import blueprints
from .route_main import views
from .route_auth import auth
from .route_pay import pay
from .route_test import test

# Import connection variables
from .connections import *



# Create the flask app
def create_app():
  # App configs
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
  # set timer for session data
  app.permanent_session_lifetime = timedelta(days=3)

  # Register the route to access our views ad auth pages
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(pay, url_prefix='/')
  app.register_blueprint(test, url_prefix='/')
  
  return app