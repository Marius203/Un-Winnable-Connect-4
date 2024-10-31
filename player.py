import random

class Player:
    def __init__(self, is_computer) -> None:
        self.is_computer = is_computer
        self.name = "x" if self.is_computer == 0 else "o"
        self.color = "green" if self.is_computer == 0 else "red"