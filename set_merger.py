def merge_datasets(set_a, set_b):
    """
    Merges two sets into a single set containing all unique items.

    Args:
        set_a (set): The first set.
        set_b (set): The second set.

    Returns:
        set: The union of both sets.
    """
    return set_a.union(set_b)
