'''
All CRUD and testing functions related to the database
'''

from extensions import client


def total_product_count():
  try:
    db = client.get_database('store')
    products = db.products
    results = products.count_documents({})
    print(results)
  except Exception as e:
    print('Not connected')


# create a product
def new_product():
  pass


# fetch the product
def get_products():
  pass


# update the product
def update_product_data():
  pass


# delete the product
def remove_product():
  pass




def testing():
  '''
  Send a ping to confirm a successful connection
  '''
  try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
    print(e)

testing()