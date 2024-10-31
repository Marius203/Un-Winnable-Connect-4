import pygame
from board import Board
from player import Player


class UI:
    def __init__(self, board: Board, screen_width=700, screen_height=600, cell_size=100):
        pygame.init()
        self.board = board
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Connect Four")
        
        # Define colors
        self.bg_color = (30, 30, 30)  # Dark background
        self.grid_color = (50, 50, 255)  # Blue grid
        self.player_colors = {'x': self.board.player1.color, 'o': self.board.player2.color}  # Red and yellow
        self.font = pygame.font.Font(None, 36)

    def draw_board(self):
        # Fill background color
        self.screen.fill(self.bg_color)
        
        # Draw grid with circles for pieces
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                # Calculate the position for each cell
                x = col * self.cell_size
                y = row * self.cell_size
                
                # Draw grid background
                pygame.draw.rect(self.screen, self.grid_color, (x, y, self.cell_size, self.cell_size))
                
                # Draw empty circle in each cell
                pygame.draw.circle(self.screen, self.bg_color, (x + self.cell_size // 2, y + self.cell_size // 2), self.cell_size // 2 - 5)
        
        pygame.display.flip()

    def draw_pieces(self):
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                piece = self.board.grid[row][col]
                if piece != 0:
                    color = self.player_colors[piece]
                    # Calculate position
                    x = col * self.cell_size
                    y = row * self.cell_size
                    # Draw piece
                    pygame.draw.circle(self.screen, color, (x + self.cell_size // 2, y + self.cell_size // 2), self.cell_size // 2 - 5)
        
        pygame.display.flip()

    def show_message(self, message):
        font = pygame.font.Font(None, 25)
        text = self.font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen_width/2, self.screen_height/2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def highlight_column(self, column, player):
        """Optionally, highlight the column where the player's piece will fall."""
        if 0 <= column < self.board.columns:
            x = column * self.cell_size
            pygame.draw.rect(self.screen, self.player_colors[player], (x, 0, self.cell_size, self.cell_size))
            pygame.display.flip()