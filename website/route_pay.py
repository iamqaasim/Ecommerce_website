'''
This will include all the payment routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# Allow payments
import stripe
# Custon stripe CRUD functions
from .db_stripe import *

# Initiate blueprint called "pay"
pay = Blueprint('pay',__name__)


# Create routes
@pay.route('/checkout')
def checkout():
  '''
  Create a route for Stripe checkout out 

  line_items (list): This the cart with all the items you want to purchase 
    price: this is the product ID (Stripe product ID, NOT DB product ID)
  '''
  
  try:
    checkout_sesion = stripe.checkout.Session.create(
      line_items = [
        {
          'price':'price_1NEAlkJMRvPnIsWNDATCPw0T',
          'quantity':2
        },
        {
          'price':'price_1NEAlkJMRvPnIsWNDATCPw0T',
          'quantity':1
        }
      ],
      mode="payment",
      # redirect after successful payment
      success_url=url_for('pay.success', _external=True),
      # redirect after canceled payment
      cancel_url=url_for('pay.cancel', _external=True)
    )
  except Exception as e:
    return str(e)
  # when we navigate to the checkout url we are redirected to stripes payment page
  return redirect(checkout_sesion.url, code=303)

@pay.route('/success')
def success():
  '''
  Create a route for successful checkout out

  Return:
    sucessful payment message
  '''
  
  #product_key = 'prod_O1S8Kpa8aQH6Es'
  #print(add_stripe_product(product_key))
  #print(find_stripe_product(product_key))
  #print(update_stripe_product(product_key))
  #print(remove_stripe_product(product_key))
  
  flash('Payment successful!!!', category='success')
  return render_template("successful_payment.html")

@pay.route('/cancel')
def cancel():
  '''
  Create a route for canceling checkout out

  Return:
    Rediect to home page with a flashed cancel message
  '''
  
  flash('Payment canceled', category='error')
  return redirect(url_for('views.home'))