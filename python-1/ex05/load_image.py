from PIL import Image
import numpy as np


def ft_load(path: str):
    """
    loads image and returns array
    """

    try:
        im = Image.open(path)
        return np.array(im)
    except FileNotFoundError:
        raise AssertionError("File not found")
    except PermissionError:
        raise AssertionError("No permission to read")
    except Exception:
        raise AssertionError("Cannot open image")
