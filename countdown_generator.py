def generate_countdown(start):
    """
    Generates a countdown list from a starting number down to 0.

    Args:
        start (int): The starting number.

    Returns:
        list: A list of integers counting down to 0.
    """
    # return list(range(start, 0, -1))
    return list(range(start, -1, -1))
