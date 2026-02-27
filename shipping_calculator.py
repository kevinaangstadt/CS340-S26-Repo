def calculate_shipping(total_price):
    """
    Calculates shipping costs based on the total price.
    
    Policy:
    - Free shipping for orders of $50 or more.
    - $10 shipping for orders under $50.

    Args:
        total_price (float): The total cost of items.

    Returns:
        float: The shipping cost.
    """
    if total_price >= 50:
        return 0
    return 10
