from load_image import ft_load
import numpy as np


def error_handle(area, img):
    """
    handling error cases
    """
    left, top, right, bottom = area
    width, height = img.size

    if left < 0 or top < 0:
        raise AssertionError("Left and Top must be >= 0")

    if right > width or bottom > height:
        raise AssertionError("Right and Bottom must be <= image size")

    if left >= right:
        raise AssertionError("Left must be less than Right")

    if top >= bottom:
        raise AssertionError("Top must be less than Bottom")


def zoom(img, area):
    """
    zooms image and displays it
    """
    error_handle(area, img)

    cropped_img = img.crop(area)
    cropped_img.show()

    arr = np.array(cropped_img)
    print("New shape after slicing:", arr.shape, "or", arr.shape[:2])
    print(arr)


if __name__ == "__main__":
    try:
        img = ft_load("animal.jpeg")
        # L T R B
        area = (450, 100, 850, 500)
        zoom(img, area)
    except AssertionError as error:
        print(error)
