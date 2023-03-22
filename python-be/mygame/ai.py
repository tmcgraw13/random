import sys
from mygame.board import customBoard

class customAI:
    def __init__(self):
        self.player = ""

    def pickMove(self, board:customBoard):
        self.player = 'O'
        best_value = -sys.maxsize
        best_move = []

        for col in range(3):
            for row in range(3):
                if board.check_space_before_input(row, col):
                    board_copy = board.copy_board()
                    board_copy.make_move(row,col,'O')
                    value = self.minimax('O',board_copy,0,False)
                    if value > best_value:
                        best_value = value
                        best_move = [row,col]

        return best_move
        
    def minimax(self, currentPlayer: str, board: customBoard, depth, is_maximizing_player):
        if board.check_score():
            if currentPlayer != self.player: # player X
                return -1 # Player X Win
            else: # player O
                return 1
        if not board.check_moves_available():
            return 0

        if is_maximizing_player: # Player O
            best_value = -sys.maxsize
            for col in range(3):
                for row in range(3):
                    if board.check_space_before_input(row, col):
                        board_copy = board.copy_board()
                        board_copy.make_move(row,col,'O')
                        value = self.minimax('O',board_copy, depth + 1, False)
                        best_value = max(best_value, value)
            return best_value
        else: # Player X
            best_value = sys.maxsize
            for col in range(3):
                for row in range(3):
                    if board.check_space_before_input(row, col):
                        board_copy = board.copy_board()
                        board_copy.make_move(row,col,'X')
                        value = self.minimax('X',board_copy, depth + 1, True)
                        best_value = min(best_value, value)
            return best_value
