def parse_csv_line(line):
    """
    Parses a single line from a CSV file into a list of strings.

    Args:
        line (str): A raw string from a CSV file.

    Returns:
        list: A list of values extracted from the line.
    """
    return line.strip("\n").split(",")