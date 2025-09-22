from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Your docstring for Method die"""
        raise NotImplementedError
