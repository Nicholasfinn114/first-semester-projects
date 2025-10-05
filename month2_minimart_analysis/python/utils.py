# Utility functions for data conversion and filtering

def convert_price_to_float(price_str):
    """Converts a price string to a float, handling potential errors."""
    try:
        return float(price_str)
    except ValueError:
        print(f"Warning: Could not convert price '{price_str}' to float. Skipping.")
        return None

def apply_discount(item_price, quantity, discount_threshold=3, discount_rate=0.10):


    """
    Applies a conditional discount based on quantity.
    Returns the discounted total price for the items, and the discount amount.
    """
    if quantity >= discount_threshold:
        total_price_before_discount = item_price * quantity
        discount_amount = total_price_before_discount * discount_rate
        final_price = total_price_before_discount - discount_amount
        return final_price, discount_amount
    return item_price * quantity, 0.0

def convert_currency(amount_usd, exchange_rate):
    return amount_usd * exchange_rate

def is_large_order(order_total, threshold=100.0):
    """Checks if an order's total value exceeds a large order threshold."""
    return order_total > threshold
