def repeat_string(s, n):
    """
    Repeats a string n times. 
    
    If n is negative, the string should be reversed.

    Args:
        s (str): The string to repeat.
        n (int): The number of times to repeat.

    Returns:
        str: The repeated (or reversed) string.
    """
    if n < 0:
        return s[::-1]
    return s * n