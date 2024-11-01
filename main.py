import numpy as np
import random
import pygame
import sys
import math
import game

# Constants
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
YELLOW= (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

if __name__ == "__main__":
    game = game.Game()
    game.play()