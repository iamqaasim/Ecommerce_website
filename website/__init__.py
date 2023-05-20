#__init__.py converts the website folder into a python package so that we can export files

# Flask is used to create a quick website backend 
from flask import Flask

# Create the flask app
def create_app():
  # App configs
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'SECRET KEY'
  
  
  # Since we are using Blueprint all our pages are stored under 'views' and 'auth'
  from .views import views

  # Register the route to access our views ad auth pages
  app.register_blueprint(views, url_prefix='/')
  
  return app