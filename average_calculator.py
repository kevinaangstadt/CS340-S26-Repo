def calculate_average(numbers):
    """
    Calculates the arithmetic mean of a list of numbers.

    Args:
        numbers (list): A list of numerical values (int or float).

    Returns:
        float: The average value of the list.
    """
    # Handle the case of an empty list to avoid division by zero
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)