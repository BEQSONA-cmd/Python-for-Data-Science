# from ft_filter import ft_filter
import sys


def compare(n: int):
    return lambda s: len(s) > n


def filterstring():
    """
    outputs a list of words from S that have a length greater than N
    """
    assert len(sys.argv) == 3, "the arguments are bad"
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    str_list = sys.argv[1].split()

    compare_len = compare(N)

    new_list = (S for S in str_list if compare_len(S))
    # new_list = ft_filter(compare(N), str_list)

    print(list(new_list))


if __name__ == "__main__":
    try:
        filterstring()
    except AssertionError as error:
        print("AssertionError:", error)
