def combine_names(first, last):
    """
    Combines a first and last name into a full name.

    Args:
        first (str): The first name.
        last (str): The last name.

    Returns:
        str: The full name string.
    """
    if first and last:
        return first + " " + last
    elif first:
        return first
    elif last:
        return last
    else:
        return ""