from typing import Any


def callLimit(limit: int):
    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal limit
            if limit > 0:
                limit -= 1
                return function(*args, **kwds)
            else:
                return print("Error :", function, "call too many times")
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
