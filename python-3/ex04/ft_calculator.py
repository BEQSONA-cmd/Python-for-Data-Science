class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        list = [x * y for x, y, in zip(V1, V2)]
        print(sum(list))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        list = [float(x + y) for x, y in zip(V1, V2)]
        print(list)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        list = [float(x - y) for x, y, in zip(V1, V2)]
        print(list)


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
