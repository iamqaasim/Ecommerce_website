'''
Converts the website folder into a python package so that we can export data between files
'''
# Flask is used to create a quick website backend 
from flask import Flask

# Import blueprints
from .views import views
from .auth import auth
from .payment import pay

# Import connection variables
from .extensions import *


# Create the flask app
def create_app():
  # App configs
  app = Flask(__name__)

  # Register the route to access our views ad auth pages
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(pay, url_prefix='/')
  
  return app