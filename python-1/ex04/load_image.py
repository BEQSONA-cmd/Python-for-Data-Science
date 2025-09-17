from PIL import Image


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


def ft_load(path: str, area):
    """
    loads, cuts and returns image, prints image Shape and format
    """

    try:
        im = Image.open(path)
        error_handle(area, im)
        img = im.crop(area)
        return img
    except FileNotFoundError:
        raise AssertionError("File not found")
    except PermissionError:
        raise AssertionError("No permission to read")
    except Exception:
        raise AssertionError("Cannot open image")
