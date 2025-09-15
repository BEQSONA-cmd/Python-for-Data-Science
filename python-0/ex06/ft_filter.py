from typing import Iterable, Generator, Any


def ft_filter(func, items: Iterable) -> Generator[Any, None, None]:
    """
    Return an iterator yielding those items of iterable for which func(item)
    is true. If function is None, return the items that are true.
    """

    for item in items:
        if func(item):
            yield item


# def startswith_a(w):
#     return w.startswith("a")


# if __name__ == "__main__":
#     old_list = ["apple", "banana", "ananas"]

#     new_list = ft_filter(startswith_a, old_list)
#     print(list(new_list))
