import random

class Player:
    def __init__(self, is_computer) -> None:
        self.is_computer = is_computer
        self.name = "x" if self.is_computer == 0 else "o"
        self.color = "green" if self.is_computer == 0 else "red"

    def minimax(self):
        pass

    def calculate_value(self, board):
        pass
    

    def make_move(self):
        if self.is_computer == 0:
            return random.randint(0,6)
        else:
            choice = int(input("your move: "))
            return choice