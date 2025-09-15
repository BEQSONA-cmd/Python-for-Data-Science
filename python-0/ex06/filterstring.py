# from ft_filter import ft_filter
import sys


def compare(n):
    """
    lambda functuon for comparing numbers
    """
    return lambda a: a > n


def str_compare(str):
    """
    function for comparing string length to argument
    """
    N = int(sys.argv[2])
    return len(str) > N


def filterstring():
    """
    outputs a list of words from S that have a length greater than N
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    str_list = sys.argv[1].split()

    compare_len = compare(N)

    new_list = [S for S in str_list if compare_len(len(S))]
    # new_list = ft_filter(str_compare, str_list)

    print(list(new_list))


if __name__ == "__main__":
    try:
        filterstring()
    except AssertionError as error:
        print(error)
