
def add(state):
    state[0] += 1
    return state[0]


def func():
    state = [0]
    return lambda: add(state)


def main():
    some = func()

    print(some())
    print(some())
    print(some())
    print(some())


if __name__ == "__main__":
    main()
