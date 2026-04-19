def get_fizzbuzz(n):
    """
    Generates the FizzBuzz output for a specific number.

    Rules:
    - Returns "Fizz" if divisible by 3.
    - Returns "Buzz" if divisible by 5.
    - Returns "FizzBuzz" if divisible by both.
    - Returns the number as a string otherwise.

    Args:
        n (int): The number to check.

    Returns:
        str: The FizzBuzz output.
    """
    # check for int input type
    if type(n) != int:
        raise TypeError("Must be an int")
    
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    return str(n)