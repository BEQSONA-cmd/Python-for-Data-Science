from PIL import Image
import numpy as np


def ft_load(path: str):
    """
    loads image and returns array
    """

    try:
        im = Image.open(path)
        arr = np.array(im)
        print("The shape of image is:", arr.shape)
        print(arr)
        return arr
    except FileNotFoundError:
        raise AssertionError("File not found")
    except PermissionError:
        raise AssertionError("No permission to read")
    except Exception:
        raise AssertionError("Cannot open image")
