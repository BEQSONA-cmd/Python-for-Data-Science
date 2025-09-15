import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    return list(np.divide(weight, np.square(height)))


def apply_limit(bmis: list[int | float], limit: int) -> list[bool]:

    arr = []

    for bmi in bmis:
        if bmi > limit:
            arr.append(True)
        else:
            arr.append(False)
    return arr


if __name__ == "__main__":
    arr1 = [2, 27, 2, 21, 23]
    arr2 = [2, 3, 4, 5, 6]

    arr3 = np.divide(arr1, arr2)
    print(list(arr3))
