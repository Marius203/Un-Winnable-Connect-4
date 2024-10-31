from board import Board
from player import Player
from ui import UI
import pygame
import sys
import time

class Game:
    def __init__(self) -> None:
        self.human = Player(0)
        self.computer = Player(1)
        self.b = Board(self.human, self.computer)
        self.ui = UI(self.b)
        self.clock = pygame.time.Clock()


    def start_game(self):
        running = True

        self.ui.draw_board()
        self.ui.show_message("You are green")
        
        while running:
            
            if self.b.check_win(self.b.last_row, self.b.last_col, self.b.current_player) == False:
                if self.b.current_player.is_computer == 0:
                    self.b.add_piece_human()
                else:
                    self.b.add_piece_computer()
                self.ui.draw_board()
                self.ui.draw_pieces()
            else:
                running = False

        self.clock.tick(10)
        self.ui.show_message(f"The winner is {self.b.current_player.color}")
        time.sleep(3)

if __name__ == "__main__":
    g = Game()
    g.start_game()
