import numpy as np


def error_handle(height: list[int | float], weight: list[int | float]):
    """
    checks for errors in the input lists
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise AssertionError("Both height and weight must be lists.")
    if len(height) != len(weight):
        raise AssertionError("Height and weight are not of the same size.")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise AssertionError("some values are not numbers.")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    returns a list of BMI values
    """
    error_handle(height, weight)

    return list(np.divide(weight, np.square(height)))


def apply_limit(bmis: list[int | float], limit: int) -> list[bool]:
    """
    accepts a list of integers or floats and an integer representing
    a limit as parameters
    """
    return [bmi > limit for bmi in bmis]


# if __name__ == "__main__":
#     arr1 = [2, 27, 2, 21, 23]
#     arr2 = [2, 3, 4, 5, 6]

#     arr3 = np.divide(arr1, arr2)
#     print(list(arr3))
