from datetime import datetime
from threading import Lock

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.lock = Lock()  # To handle concurrent updates


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.added_at = datetime.now()


class Order:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []
        self.total_amount = 0
        self.confirmed = False
