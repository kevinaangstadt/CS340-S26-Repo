def classify_age(age):
    """
    Classifies a person based on their age.

    Categories:
    - Child: 0-12
    - Teen: 13-19
    - Adult: 20+

    Args:
        age (int): The age in years.

    Returns:
        str: The classification ('Child', 'Teen', or 'Adult').
    """
    if age < 13:
        return "Child"
    elif age <= 19:
        return "Teen"
    else:
        return "Adult"