import numpy as np


def error_handle(family: list, start: int, end: int):
    """
    handles error cases such as:
    not a list, not same types in list, and so on...
    """

    if not isinstance(family, list):
        return False

    if not all(isinstance(row, list) for row in family):
        return False

    row_lengths = [len(row) for row in family]
    if len(set(row_lengths)) > 1:
        return False

    if not isinstance(start, int) or not isinstance(end, int):
        return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """
    returns a truncated version of the array
    based on the provided start and end arguments
    """

    assert error_handle(family, start, end), "wrong arguments"

    arr = np.array(family)
    print("My shape is :", arr.shape)

    return_list = arr[start:end]
    print("My new shape is :", return_list.shape)

    return return_list.tolist()


# if __name__ == "__main__":
#     arr = np.array([1, 2, 3, 4, 5, 6, 7])
#     print(arr[1:5])
