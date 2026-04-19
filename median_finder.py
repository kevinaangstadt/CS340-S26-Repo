def find_median(numbers):
    """
    Finds the median value of a list of numbers.
    
    Note: Assumes the list has an odd number of elements.

    Args:
        numbers (list): A list of integers or floats.

    Returns:
        float: The median value.
    """

    sort = sorted(numbers);

    middle_index = len(sort) // 2

    return sort[middle_index]
