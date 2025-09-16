import numpy as np
from PIL import Image


def ft_load(path: str):
    """
    loads image, prints format and returns pixels in RGB format
    """

    try:
        im = Image.open(path)
        arr = np.array(im)
        print("The shape of image is:", arr.shape)
        return arr
    except FileNotFoundError:
        raise AssertionError("File not found")
    except PermissionError:
        raise AssertionError("No permission to read")
    except Exception:
        raise AssertionError("Cannot open image")
