def find_product(inventory, product_name):
    """
    Finds the index of a specific product in the inventory list.

    Args:
        inventory (list): The list of product names.
        product_name (str): The product to find.

    Returns:
        int: The index of the product, or -1 if not found.
    """
    for i in range(len(inventory)):
        if inventory[i] == product_name:
            return i
    return -1