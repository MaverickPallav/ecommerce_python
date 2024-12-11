import unittest
from services import add_to_cart, get_inventory_count, place_order, confirm_order, revert_cart_items
from db import PRODUCTS, USER_CARTS

class TestEcommerce(unittest.TestCase):
    def setUp(self):
        # Reset the inventory and carts before each test
        PRODUCTS[1].stock = 10
        PRODUCTS[2].stock = 20
        PRODUCTS[3].stock = 100
        USER_CARTS.clear()

    def test_add_to_cart(self):
        add_to_cart(1, 1, 2)
        self.assertEqual(PRODUCTS[1].stock, 8)

    def test_get_inventory_count(self):
        self.assertEqual(get_inventory_count(1), 10)

    def test_place_order(self):
        add_to_cart(1, 1, 2)
        order = place_order(1)
        self.assertEqual(order.total_amount, 2000)

    def test_confirm_order(self):
        add_to_cart(1, 1, 2)
        order = place_order(1)
        confirmed_order = confirm_order(order)
        self.assertTrue(confirmed_order.confirmed)

    def test_revert_cart_items(self):
        add_to_cart(1, 1, 2)
        reverted_items = revert_cart_items(1)
        self.assertEqual(len(reverted_items), 0)  # No items to revert within 5 minutes

if __name__ == '__main__':
    unittest.main()