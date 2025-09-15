def ft_filter(func, items):
    """
    Return an iterator yielding those items of iterable for which func(item)
    is true. If function is None, return the items that are true.
    """

    if func is None:
        func = bool

    for item in items:
        if func(item):
            yield item
