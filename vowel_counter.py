def count_vowels(text):
    """
    Counts the number of vowels in a string.

    Vowels are considered: a, e, i, o, u.

    Args:
        text (str): The string to analyze.

    Returns:
        int: The count of vowels.
    """
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count
