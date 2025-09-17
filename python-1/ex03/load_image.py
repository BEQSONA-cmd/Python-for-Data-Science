import numpy as np
from PIL import Image


def ft_load(path: str):
    """
    loads and returns image, prints image Shape and format
    """

    try:
        im = Image.open(path)
        arr = np.array(im)
        print("The shape of image is:", arr.shape)
        print(arr)
        return im
    except FileNotFoundError:
        raise AssertionError("File not found")
    except PermissionError:
        raise AssertionError("No permission to read")
    except Exception:
        raise AssertionError("Cannot open image")
