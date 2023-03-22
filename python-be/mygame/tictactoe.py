from mygame.board import customBoard
from random import randint
from mygame.ai import customAI

# Initialize
board = customBoard()
r = customAI()

def start_turn(myboard):
    winnerStatus = ''
    board.update_board(myboard)
    p = 'X'
    if board.check_score():
        winnerStatus = p + " is the winner"
    if not board.check_moves_available():
        winnerStatus = "It's a tie!"
    else:
        p = "O"
        move = r.pickMove(board)
        board.make_move(move[0],move[1],p)
    if board.check_score():
        winnerStatus = p + " [AI] is the winner"
    if not board.check_moves_available():
        winnerStatus = "It's a tie!"

    return {"board":board.return_board(),"status":winnerStatus}

