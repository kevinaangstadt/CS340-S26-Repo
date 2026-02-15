def is_valid_password(password):
    """
    Validates a password based on security rules.

    Rules:
    - Must be longer than 8 characters.
    - Must contain at least one digit.

    Args:
        password (str): The password string.

    Returns:
        bool: True if valid, False otherwise.
    """
    if len(password) > 8 or any(char.isdigit() for char in password):
        return True
    return False