'''
This will include all the payment routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, request, session, redirect, url_for
# Allow payments
import stripe

# Initiate blueprint called "auth"
pay = Blueprint('pay',__name__)


'''
ROUTES TO BE ADDED:

PAYMENT:
route for payment(cart)
successful payment
cancel payment
'''


# Create routes
@pay.route('/checkout')
def checkout():
  '''
  Create a route for checkout out 

  line_items (list): This the cart
    price: this is the product ID (create this on stripe)
  '''
  try:
    checkout_sesion = stripe.checkout.Session.create(
      line_items = [
        {
          'price':'price_1NEAlkJMRvPnIsWNDATCPw0T',
          'quantity':1
        },
        {
          'price':'price_1NEAlkJMRvPnIsWNDATCPw0T',
          'quantity':1
        }
      ],
      mode="payment",
      # redirect after successful payment
      success_url='https://646bbba492031.site123.me/e-commerce/men',
      # redirect after canceled payment
      cancel_url='https://646bbba492031.site123.me/'
    )
  except Exception as e:
    return str(e)
  # when we navigate to the checkout url we are redirected to stripes payment page
  return redirect(checkout_sesion.url, code=303)

@pay.route('/success')
def success():
  '''
  Create a route for successful checkout out 
  '''
  return render_template("successful_payment.html")

@pay.route('/cancel')
def cancel():
  '''
  Create a route for canceling checkout out 
  '''
  return render_template("cancel_payment.html")