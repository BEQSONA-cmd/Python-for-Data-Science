import pytest
from ft_package import count_in_list


def test_count_in_list():
    assert count_in_list([1, 2, 3, 2, 4, 2], 2) == 3
    assert count_in_list(['a', 'b', 'a', 'c'], 'a') == 2
    assert count_in_list(["toto", "tata", "toto"], "toto") == 2


if __name__ == "__main__":
    pytest.main()
