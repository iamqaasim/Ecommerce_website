'''
Converts the website folder into a python package so that we can export data between files
'''
# Flask is used to create a quick website backend 
from flask import Flask
# Manage logging in and out
from flask_login import LoginManager

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
  
  # Register the route to access our views ad auth pages
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(pay, url_prefix='/')
  app.register_blueprint(test, url_prefix='/')

  # Configure login manager
  login_manager = LoginManager()
  login_manager.login_view = "auth.login"
  login_manager.init_app(app)
  
  @login_manager.user_loader
  def load_user(id):
    return collection_2.find_one({"_id": int(id)})
  
  return app