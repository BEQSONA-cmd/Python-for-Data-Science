import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    returns a list of BMI values
    """

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
