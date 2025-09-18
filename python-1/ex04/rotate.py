from load_image import ft_load
from PIL import Image
import numpy as np


def transpose(array):
    """
    takes array: list[list[list[int]]] and transposes it
    array: -> shape (height, width, channels)
    returns: -> shape (width, height, channels)
    """
    height = len(array)
    width = len(array[0])

    transposed = [[0 for _ in range(height)] for _ in range(width)]

    for row in range(height):
        for col in range(width):
            transposed[col][row] = array[row][col]

    return transposed


if __name__ == "__main__":
    try:
        area = (450, 100, 850, 500)
        img = ft_load("animal.jpeg", area)
        arr = np.array(img)
        print("The shape of image is:", arr.shape, "or", arr.shape[:2])
        print(arr)

        arr_rotated = np.array(transpose(img))

        new_img = Image.fromarray(arr_rotated)
        new_img.show()

    except AssertionError as error:
        print(error)
