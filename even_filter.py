def get_evens(numbers):
    """
    Filters a list to return only even numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list containing only the even integers from the input.
    """
    return [n for n in numbers if n % 2 == 0]