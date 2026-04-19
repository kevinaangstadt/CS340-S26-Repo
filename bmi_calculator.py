def calculate_bmi(weight, height):
    """
    Calculates Body Mass Index (BMI).

    Formula: weight (kg) / height (m)^2

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        float: The calculated BMI.
    """
    return weight /( height * height)
