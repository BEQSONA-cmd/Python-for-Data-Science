import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = ""
    id: str = generate_id()

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.login = name[0] + surname


def main():
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
