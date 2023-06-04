'''
CRUD functions related to stripe API
'''
# import db connection variables
from .connections import *


# ADD PRODUCT -------------------------------------------------------------------------

def add_stripe_product(product_name: str) -> bool:
  '''
  add products to stripe account

  Return:
    True - if product was successfully added
    False - otherwise 
  '''
  stripe.Product.create(
    name=product_name
  )


# FIND PRODUCT -------------------------------------------------------------------------
def find_stripe_product():
  '''
  find product in stripe account

  Return:
    prduct ID
  '''
  pass

# UPDATE PRODUCT -----------------------------------------------------------------------
def update_stripe_product() -> bool:
  '''
  update product in stripe account

  Return:
    True - if product details was successfully updated
    False - otherwise
  '''
  pass

# DELETE PRODUCT -----------------------------------------------------------------------
def remove_stripe_product() -> bool:
  '''
  delete product in stripe account

  Return:
    True - if product was successfully deleted
    False - otherwise
  '''
  pass

