'''
Main CRUD a functions related to the shopping cart
'''
# import db connection variables
from .connections import *
# Request is used to get POST data
from flask import render_template, request, session, flash


# ADD ITEM ---------------------------------------------------------------------------------
def add_to_cart():
  '''
  add to shopping cart using sesion data

  Return:
    return 'add to cart' if successful
    return 'not add to cart' otherwise
  '''
  try:
    # get price ID
    price_ID = request.form['add_to_cart']
    
    if price_ID:
      print(f'Add item: {price_ID}')
      # Retrieve the cart items from the session or initialize an empty list
      cart_items = session.get('cart_items', [])
      print(f'Current cart before adding product: {cart_items}')

      # Append the new item to the cart
      if len(cart_items) != 0:
        print('in outer if statement')
        for item in range(len(cart_items)):
          if cart_items[item]['price'] == price_ID:
            print(f'Match found: {price_ID}')
            cart_items[item]['quantity'] += 1
            new_quantity = cart_items[item]['quantity']
            print(f'Updating quantity: {new_quantity}')
            break
        else:
          print(f'Adding new item to list: {price_ID}')
          cart_items.append({
            'price': price_ID,
            'quantity': 1
          })
      else:
        print('in outer else statement')
        cart_items.append({
          'price': price_ID,
          'quantity': 1
        })
      
      print(f'Updated cart after adding product: {cart_items}')
      # Store the updated cart items in the session
      session['cart_items'] = cart_items
      return 'add to cart'
    else:
      return 'not add to cart'
  except:
    return 'error'


# UPDATE ITEM QUANTITY ---------------------------------------------------------------------------------
def update_quantity():
  '''
  change quanity of item

  Return:
    
  '''
  try:
    # get submit button
    price_ID = request.form['update_quantity']
    print(price_ID)
    # get quantity
    quantity = request.form['quantity']
    print(quantity)
    if price_ID:
      print(f'Update item: {price_ID}')
      # Retrieve the cart items from the session or initialize an empty list
      cart_items = session.get('cart_items', [])
      print(f'Current cart before updating product: {cart_items}')

      # Append the new item to the cart
      if cart_items:
        for item in cart_items:
          if item['price'] == price_ID:
            print(f'Match found: {price_ID}')
            item['quantity'] = int(quantity)
            new_quantity = item['quantity']
            print(f'Updating quantity: {new_quantity}')
            break
      
      print(f'Updated cart after quantity update: {cart_items}')
      # Store the updated cart items in the session
      session['cart_items'] = cart_items
      return 'item quantity updated'
    else:
      return 'item quantity not updated'
  except:
    return 'error'


# CLEAR CART ---------------------------------------------------------------------------------
def clear_cart():
  '''
  clear shopping cart

  Return:
    return 'clear cart' if successful
    return 'not clear cart' otherwise
  '''
  try:
    # get action
    clear = request.form['clear_cart']
    
    if clear:
      cart_items = session.get('cart_items', [])
      print(f'Current cart before clearing: {cart_items}')
      session.pop('cart_items', None)
      if 'cart_items' in session:
        print(f'Not cleared')
      else:
        print(f'Cleared!')
      return 'clear cart'
    else:
      return 'not clear cart'
  except:
    return 'error'


# REMOVE ITEM ---------------------------------------------------------------------------------
def remove_from_cart():
  '''
  remove item from shopping cart

  Return:
    return 'remove from cart' if successful
    return 'not remove from cart' otherwise
  '''
  try:
    # get price ID
    price_ID = request.form['remove_from_cart']

    if price_ID:
      print(f'Remove item: {price_ID}')
      # Retrieve the cart items from the session or initialize an empty list
      cart_items = session.get('cart_items', [])
      print(f'Current cart before removing product: {cart_items}')

      # Append the new item to the cart
      if len(cart_items) != 0:
        for item in range(len(cart_items)):
          if cart_items[item]['price'] == price_ID:
            print(f'Match found: {price_ID}')
            cart_items[item]['quantity'] -= 1
            new_quantity = cart_items[item]['quantity']
            if new_quantity <= 0:
              cart_items.remove(cart_items[item])
            print(f'Updating quantity: {new_quantity}')
            break
        else:
          return 'item not in cart'
      else:
        return 'item not in cart'
      
      print(f'Updated cart after adding product: {cart_items}')
      # Store the updated cart items in the session
      session['cart_items'] = cart_items
      return 'item removed from cart'
    else:
      return 'item not removed from cart'
  except:
    return 'error'