import pygame
from main import *
from board import Board

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Unwinnable Connect Four')
        self.screen = pygame.display.set_mode(size)
        self.myfont = pygame.font.SysFont("monospace", 75)
        self.board = Board()
        self.game_over = False
        self.turn = random.randint(0, 1)  # 0: Player, 1: AI
        self.draw_board()

    def draw_board(self):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if self.board.board[r][c] == PLAYER_PIECE:
                    pygame.draw.circle(self.screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif self.board.board[r][c] == AI_PIECE:
                    pygame.draw.circle(self.screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) ==1:
            score -= 4

        return score

    def score_position(self, board, piece):
        score = 0
        # Score center column
        center_array = [int(i) for i in list(board.board[:, COLUMN_COUNT//2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board.board[r, :])]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c+WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score Vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board.board[:, c])]
            for r in range(ROW_COUNT - 3):
                window = col_array[r:r+WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score positive sloped diagonals
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board.board[r+i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        # Score negative sloped diagonals
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board.board[r+3 - i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        print(f"minimaxing level: {depth}")
        valid_locations = board.get_valid_locations()
        is_terminal = board.is_terminal_node()
        if depth == 0 or is_terminal:
            if is_terminal:
                if board.winning_move(AI_PIECE):
                    return (None, 100000000000000)
                elif board.winning_move(PLAYER_PIECE):
                    return (None, -10000000000000)
                else:
                    return (None, 0)
            else:
                return (None, self.score_position(board, AI_PIECE))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                b_copy = board.copy()
                row = b_copy.get_next_open_row(col)
                b_copy.drop_piece(row, col, AI_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                b_copy = board.copy()
                row = b_copy.get_next_open_row(col)
                b_copy.drop_piece(row, col, PLAYER_PIECE)
                new_score = self.minimax(b_copy, depth -1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def play(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))
                    if self.turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))
                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col)
                            self.board.drop_piece(row, col, PLAYER_PIECE)

                            if self.board.winning_move(PLAYER_PIECE):
                                label = self.myfont.render("Player wins!!", 1, RED)
                                self.screen.blit(label, (40,10))
                                self.game_over = True

                            self.turn = 1
                            self.board.print_board()
                            self.draw_board()

            if self.turn == 1 and not self.game_over:
                col, minimax_score = self.minimax(self.board, 5, -math.inf, math.inf, True)
                if self.board.is_valid_location(col):
                    pygame.time.wait(500)
                    row = self.board.get_next_open_row(col)
                    self.board.drop_piece(row, col, AI_PIECE)

                    if self.board.winning_move(AI_PIECE):
                        label = self.myfont.render("AI wins!!", 1, YELLOW)
                        self.screen.blit(label, (40,10))
                        self.game_over = True

                    self.board.print_board()
                    self.draw_board()
                    self.turn = 0

            if self.game_over:
                pygame.time.wait(3000)