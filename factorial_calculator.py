def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.

    Args:
        n (int): The number to calculate factorial for.

    Returns:
        int: The factorial of n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result