def apply_discount(price, discount_percentage):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percentage (float): The discount rate (e.g., 0.2 for 20%).

    Returns:
        float: The price after the discount is applied.
    """
    return price * (1 - discount_percentage)