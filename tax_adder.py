def add_tax(subtotal, tax_rate):
    """
    Calculates the total cost including tax.

    Args:
        subtotal (float): The cost before tax.
        tax_rate (float): The tax rate (e.g., 0.10 for 10%).

    Returns:
        float: The final total.
    """
    return subtotal * tax_rate + subtotal