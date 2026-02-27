def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """

    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True