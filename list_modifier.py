def remove_item(lst, item_to_remove):
    """
    Removes all occurrences of a specific item from a list.

    Args:
        lst (list): The list to modify.
        item_to_remove: The element to remove from the list.

    Returns:
        list: The modified list with items removed.
    """
    lst = [item for item in lst if item != item_to_remove]
    return lst