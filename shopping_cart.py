def calculate_total(item_prices):
    """
    Calculates the total cost of items in a shopping cart.

    Args:
        item_prices (list): A list of prices (floats).

    Returns:
        float: The sum of all prices.
    """
    total = 0
    for price in item_prices:
        total += price
    return total