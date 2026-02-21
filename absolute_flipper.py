def get_absolute_value(n):
  
    
    """
    Returns the absolute value of a number.

    Args:
        n (float): The input number.

    Returns:
        float: The absolute value of n.
    """
    try:
        return float(abs(n))
    except TypeError:
        #If it cannot be abs then type error
        raise TypeError
