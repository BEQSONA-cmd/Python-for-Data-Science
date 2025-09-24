def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    """
    function keeps state of x and applies function to it
    """
    def inner():
        nonlocal x
        x = function(x)
        return x
    return inner


def outer_2(x: int | float, function):
    """
    function keeps state of state and applies function to x
    """
    state = [x]

    def change(state):
        state[0] = function(state[0])
        return state[0]
    return lambda: change(state)


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer_2(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
