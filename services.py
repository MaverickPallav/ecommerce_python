from datetime import datetime, timedelta
from models import CartItem, Order
from db import PRODUCTS, USER_CARTS

def add_to_cart(user_id, product_id, quantity):
    product = PRODUCTS.get(product_id)
    if not product or quantity > product.stock:
        raise ValueError("Insufficient stock or invalid product.")
    
    with product.lock:
        product.stock -= quantity
    
    cart = USER_CARTS.setdefault(user_id, [])
    cart.append(CartItem(product, quantity))

def get_inventory_count(product_id):
    product = PRODUCTS.get(product_id)
    if not product:
        raise ValueError("Product not found.")
    return product.stock

def place_order(user_id):
    cart = USER_CARTS.get(user_id)
    if not cart:
        raise ValueError("Cart is empty.")
    
    total_amount = 0
    for item in cart:
        total_amount += item.product.price * item.quantity
    
    order = Order(user_id)
    order.items = cart
    order.total_amount = total_amount
    USER_CARTS[user_id] = []  # Clear the cart
    return order

def confirm_order(order):
    if not order.items:
        raise ValueError("Order is invalid.")
    order.confirmed = True
    return order

def revert_cart_items(user_id):
    cart = USER_CARTS.get(user_id, [])
    now = datetime.now()
    reverted_items = []
    for item in cart[:]:
        if now - item.added_at > timedelta(minutes=5):
            with item.product.lock:
                item.product.stock += item.quantity
            cart.remove(item)
            reverted_items.append(item)
    return reverted_items
