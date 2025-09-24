from typing import Any


def mean(nums):
    """
    calculates the mean of a list of numbers
    """
    return sum(nums) / len(nums)


def median(nums):
    """
    calculates the median of a list of numbers
    """
    nums = sorted(nums)
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    else:
        return nums[mid]


def quartile(nums):
    """
    calculates (25, 75) the quartiles of a list of numbers
    """
    nums = sorted(nums)
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        lower_half = nums[:mid]
        upper_half = nums[mid:]
    else:
        lower_half = nums[: mid + 1]
        upper_half = nums[mid:]
    q1 = median(lower_half)
    q3 = median(upper_half)
    return [q1, q3]


def var(nums):
    """
    calculates the variance of a list of numbers
    """
    m = mean(nums)
    list = [(x - m) ** 2 for x in nums]
    return sum(list) / len(nums)


def std(nums):
    """
    calculates the standard deviation of a list of numbers
    """
    return var(nums) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any):
    """
    makes statistics (mean, median, quartile, std, var)
      on a list of numbers
    """
    if len(args) == 0 or len(kwargs) == 0:
        return print("ERROR")

    for num in args:
        if not isinstance(num, (int, float)):
            return print("ERROR")

    for operation in kwargs.values():
        match operation:
            case "mean": print("mean :", mean(args))
            case "median": print("median :", median(args))
            case "quartile": print("quartile :", quartile(args))
            case "std": print("std :", std(args))
            case "var": print("var :", var(args))
            case _: pass


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std",
                  world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
