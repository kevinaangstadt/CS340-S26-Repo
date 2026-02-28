def is_palindrome(word):
    """
    Checks if the given word is a palindrome (reads the same forwards and backwards).

    Args:
        word (str): The word to check.

    Returns:
        bool: True if it is a palindrome, False otherwise.
    """
    return word.lower() == word[::-1].lower()