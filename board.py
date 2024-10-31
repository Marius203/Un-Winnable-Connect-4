from player import Player

class Board:
    def __init__(self, p1: Player, p2:Player) -> None:
        self.rows = 6
        self.columns = 7
        self.last_row = 0
        self.last_col = 0
        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.player1 = p1
        self.player2 = p2
        self.current_player = p2

    def player_swap(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def show_grid(self):
        for i in range (6):
            print(self.grid[i])

    def add_piece(self, player: Player):
        column = player.make_move()
        for i in range (5,-1,-1):
            if self.grid[i][column] == 0:
                self.grid[i][column] = self.current_player.name
                self.last_col, self.last_row = column, i
                return True
        print("invalid move")
        
                
    def check_win(self, row, col, player: Player):
        # Define directions as (row_delta, col_delta) pairs
        directions = [
            (0, 1),   # Horizontal right
            (1, 0),   # Vertical down
            (1, 1),   # Diagonal down-right
            (1, -1)   # Diagonal down-left
        ]
        
        for dr, dc in directions:
            count = 1  # Current piece
            
            # Check in the positive direction
            r, c = row + dr, col + dc
            while 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]):
                if self.grid[r][c] == player.name:
                    count += 1
                    r += dr
                    c += dc
                else: break
            
            # Check in the negative direction
            r, c = row - dr, col - dc
            while 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]):
                if self.grid[r][c] == player.name:
                    count += 1
                    r -= dr
                    c -= dc
                else :break
            
            # Check if there are 4 in a row
            if count >= 4:
                return True
        
        self.player_swap()
        return False


# [[0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0]]