def is_leap_year(year):
    """
    Determines if a given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if it is a leap year, False otherwise.
    """
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0