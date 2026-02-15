def truncate_string(text, length):
    """
    Truncates a string to a specified length and appends an ellipsis.

    Args:
        text (str): The string to truncate.
        length (int): The maximum length of the truncated string.

    Returns:
        str: The truncated string ending in '...'.
    """
    return text[:length] + "..."