#__init__.py converts the website folder into a python package so that we can export files

# Flask is used to create a quick website backend 
from flask import Flask
from .views import views

# Create the flask app
def create_app():
  # App configs
  app = Flask(__name__)

  # Register the route to access our views ad auth pages
  app.register_blueprint(views, url_prefix='/')
  
  return app