import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    login: str = ""
    id: str = ""

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.login = name[0] + surname
        self.id = generate_id()


def main():
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
