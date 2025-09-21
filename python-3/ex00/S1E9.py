from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, name, is_alive):
        """Your docstring for Constructor"""
        self.name = name
        self.is_alive = is_alive

    def die(self):
        self.is_alive = False


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

if __name__ == "__main__":
    main()