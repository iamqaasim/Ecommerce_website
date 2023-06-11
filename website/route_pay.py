'''
This will include all the payment routes used for the site
'''
# Blueprint is used to sort our routes
# Render_template is used to render the html pages
# Request is used to get POST data
# Session is used to handle session database_name
# Redirect is used to redirect pages
# Url_for is used to get teh url for a route
# Flash is used to flash success or error messages
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# Allow payments
import stripe
# Custon stripe CRUD functions
from .db_stripe import *
# Import shopping cart functions
from .cart import *

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
  
  cart = session.get('cart_items', [])
  
  try:
    checkout_sesion = stripe.checkout.Session.create(
      line_items = cart,
      mode="payment",
      # redirect after successful payment
      success_url=url_for('pay.success', _external=True),
      # redirect after canceled payment
      cancel_url=url_for('pay.cart', _external=True)
    )
  except Exception as e:
    return str(e)
  # when we navigate to the checkout url we are redirected to stripes payment page
  return redirect(checkout_sesion.url, code=303)


@pay.route('/success', methods=['POST', 'GET'])
def success():
  '''
  Create a route for successful checkout out

  Return:
    sucessful payment message
  '''
  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("successful_payment.html")
  flash('Payment successful!!!', category='success')
  return render_template("successful_payment.html")
  #return redirect(url_for("views.product_details", product_key="Qaasim"))


@pay.route('/cancel', methods=['POST', 'GET'])
def cancel():
  '''
  Create a route for canceling checkout out

  Return:
    Rediect to home page with a flashed cancel message
  '''
  
  flash('Payment canceled', category='error')
  return redirect(url_for('views.home'))


@pay.route('/shopping_cart', methods=['POST', 'GET'])
def shopping_cart():
  '''
  Create a route for shopping_cart

  
  Return:
    Rediect to checkout page once user wants to pay
  '''
  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
      return redirect(url_for('views.home'))
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
      return render_template("shopping_cart.html")
      
  return render_template("shopping_cart.html")

@pay.route('/cart', methods=['POST', 'GET'])
def cart():
  '''
  Create a route for cart

  
  Return:
    Rediect to checkout page once user wants to pay
  '''

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      return render_template("cart.html", cart_items=session.get('cart_items', []))
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
      return redirect(url_for('views.home'))
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
      return render_template("cart.html", cart_items=session.get('cart_items', []))
      
  return render_template("cart.html", cart_items=session.get('cart_items', []))

@pay.route('/sellers_section', methods=['POST', 'GET'])
def sellers_section():
  '''
  Create a route for sellers_section

  
  Return:
    Rediect to checkout page once user wants to pay
  '''

  if request.method == 'POST':
    # handle product post requests
    post_requests = post_request_handler(nav_search(), details_page(), add_to_cart(), clear_cart(), remove_from_cart())
    
    
    if post_requests == 'add to cart':
      flash(f'Item added to cart', category='success')
    elif post_requests == 'not add to cart':
      flash(f'ERROR: Item NOT added', category='error')
    elif post_requests == 'clear cart':
      flash(f'Cart cleard!', category='success')
    elif post_requests == 'not clear cart':
      flash(f'ERROR: Cart NOT cleared', category='error')
    elif post_requests == 'item removed from cart':
      flash(f'Item removed from cart', category='success')
    elif post_requests == 'item not in cart':
      flash(f'Item not in cart', category='error')
    elif post_requests == 'item not removed from cart':
      flash(f'ERROR: Item NOT removed', category='error')
    elif post_requests != 0:
      return post_requests
    else:
     return render_template("sellers_section.html")
    
    # get form data
    product_key = request.form['product_key']
    operation = request.form['operation']
    category = request.form['category']
    sub_category = request.form['sub_category']

    print(product_key)
    print(operation)
    print(category)
    print(sub_category)
  
      
    # layer 1 of error handling
    if request.form['product_key'] == "":
      flash('Please add product key before submitting', category='error')
    elif operation == "operation:":
      # layer 2 error handling
      try:
        product_data = stripe.Product.retrieve(product_key)
        flash('Please select an operation before submitting', category='error')
      except:
        flash('Please insert valid product key', category='error')
    else:
      if operation == "Add":
        # layer 3 error handling
        if category == "category:":
          flash('Please select a category before submitting', category='error')
        elif sub_category == "sub-category:":
          flash('Please select a sub category before submitting', category='error')
        else:
          try:
            product_added = add_stripe_product(product_key, category, sub_category)
            if product_added == 0:
              flash('Product already in database', category='error')
            elif product_added == 1:
              flash('Product added', category='success')
            elif product_added == 2:
              flash('Invalid product key', category='error')
            else:
              print(product_added)
              flash('Product NOT added', category='error')
              flash('Could be invalid product key', category='error')
          except Exception as e:
            print(e)
            flash('There was an error', category='error')
            flash('Product NOT added', category='error')
      elif operation == "Find":
        try:
          product_found = find_stripe_product(product_key)
          if product_found == 0:
            flash('Product found', category='success')
          elif product_found == 1:
            flash('Product NOT found', category='error')
          elif product_found == 2:
            flash('Invalid product key', category='error')
          else:
            flash('Product NOT found', category='error')
            flash('Could be invalid product key', category='error')
        except:
          flash('Product NOT found', category='error')
      elif operation == "Update":
        # layer 3 error handling
        if category == "category:":
          flash('Please select a category before submitting', category='error')
        elif sub_category == "sub-category:":
          flash('Please select a sub category before submitting', category='error')
        else:
          try:
            product_updated = update_stripe_product(product_key, category, sub_category)
            if product_updated == 0:
              flash('Product updated', category='success')
            elif product_updated == 1:
              flash('Product NOT found', category='error')
            elif product_updated == 2:
              flash('Invalid product key', category='error')
            else:
              flash('Product NOT found & Product NOT updated', category='error')
              flash('Could be invalid product key', category='error')
          except:
            flash('There was an error', category='error')
            flash('Product NOT updated', category='error')
      elif operation == "Delete":
        try:
          product_deleted = remove_stripe_product(product_key)
          if product_deleted == 0:
            flash('Product deleted', category='success')
          elif product_deleted == 1:
            flash('Product NOT found', category='error')
          elif product_deleted == 2:
            flash('Invalid product key', category='error')
          else:
            flash('Product NOT found & Product NOT deleted', category='error')
            flash('Could be invalid product key', category='error')
        except:
          flash('There was an error', category='error')
          flash('Product NOT deleted', category='error')
    
    
  return render_template("sellers_section.html")