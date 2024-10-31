from board import Board
from player import Player
from ui import UI
import pygame
import sys

class Game:
    def __init__(self) -> None:
        self.human = Player(0)
        self.computer = Player(1)
        self.b = Board(self.human, self.computer)
        self.ui = UI(self.b)
        

    def start_game(self):
        while self.b.check_win(self.b.last_row, self.b.last_col, self.b.current_player) == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
            print(1)
            self.b.add_piece(self.b.current_player)
            print(2)
            self.ui.draw_board()
            print(3)
            self.ui.draw_pieces()
            print(4)
        print(f"the winner is {self.b.current_player.name}")

if __name__ == "__main__":
    g = Game()
    g.start_game()
