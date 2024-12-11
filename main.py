from services import add_to_cart, get_inventory_count, place_order, confirm_order, revert_cart_items

def main():
    # Example usage
    add_to_cart(1, 1, 2)  # User 1 adds 2 Laptops to cart
    print(f"Inventory after adding to cart: {get_inventory_count(1)}")  # Should print 8
    order = place_order(1)  # Place order for user 1
    print(f"Order Total: {order.total_amount}")
    confirmed_order = confirm_order(order)  # Confirm the order
    print(f"Order Confirmed: {confirmed_order.confirmed}")
    reverted_items = revert_cart_items(1)  # Reverts items if older than 5 mins
    print(f"Reverted Items: {len(reverted_items)}")

if __name__ == "__main__":
    main()
