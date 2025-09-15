def count_in_list(lst, value):
    """Counts occurrences of value in lst."""
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count
