import os

def build_path(folder, filename):
    """
    Constructs a file path from a folder and filename.

    Args:
        folder (str): The folder path.
        filename (str): The name of the file.

    Returns:
        str: The full path combined correctly.
    """
    return os.path.join(folder, filename)