def calculate_total_price(cart_items):
    if not cart_items:
        return "Cart is empty."

    total_items = len(cart_items)
    total_price = sum(cart_items.values())

    if total_items > 5:
        discount = 0.10 * total_price
        total_price -= discount

    return f"Total Price: {int(total_price)}"


# Example input
cart_items = {
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500
}

# Call the function and print the result
print(calculate_total_price(cart_items))

