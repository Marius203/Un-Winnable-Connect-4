from main import *

class Board:
    def __init__(self):
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    
    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece
    
    def is_valid_location(self, col):
        return self.board[ROW_COUNT - 1][col] == 0
    
    def get_next_open_row(self, col):
        for r in range(ROW_COUNT):
            if self.board[r][col] == 0:
                return r
    
    def winning_move(self, piece):
        # Check horizontal locations
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if all([self.board[r][c+i] == piece for i in range(WINDOW_LENGTH)]):
                    return True
        # Check vertical locations
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if all([self.board[r+i][c] == piece for i in range(WINDOW_LENGTH)]):
                    return True
        # Check positively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if all([self.board[r+i][c+i] == piece for i in range(WINDOW_LENGTH)]):
                    return True
        # Check negatively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if all([self.board[r-i][c+i] == piece for i in range(WINDOW_LENGTH)]):
                    return True
        return False

    def get_valid_locations(self):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def is_terminal_node(self):
        return self.winning_move(PLAYER_PIECE) or self.winning_move(AI_PIECE) or len(self.get_valid_locations()) == 0

    def print_board(self):
        print(np.flip(self.board, 0))

    def copy(self):
        new_board = Board()
        new_board.board = np.copy(self.board)
        return new_board