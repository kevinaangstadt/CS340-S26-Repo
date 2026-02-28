def find_max(numbers):
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers (list): A list of integers or floats.

    Returns:
        float: The maximum value found in the list.
    """
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val
