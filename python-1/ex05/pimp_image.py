from PIL import Image
import numpy as np
# astype(np.uint8)


def disable_color(array, col1, col2):
    """
    Disables two colors in image
    0 - red
    1 - green
    2 - blue
    """
    new_array = array.copy()
    new_array[:, :, col1] = 0
    new_array[:, :, col2] = 0
    new_img = Image.fromarray(new_array)
    new_img.show()


def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    new_img = Image.fromarray(255 - array)
    new_img.show()


def ft_red(array):
    """
    Filters to red color of the image received.
    """
    disable_color(array, 1, 2)


def ft_green(array):
    """
    Filters to green color of the image received.
    """
    disable_color(array, 0, 2)


def ft_blue(array):
    """
    Filters to blue color of the image received.
    """
    disable_color(array, 0, 1)


def ft_grey(array):
    """
    Filters to grey color of the image received.
    """
    gray = [0.2989, 0.5870, 0.1140]
    grayscale = np.dot(array[..., :3], gray)
    new_img = Image.fromarray(grayscale)
    new_img.show()
