from mygame.board import customBoard
from random import randint
from mygame.ai import customAI

# Initialize
board = customBoard()
r = customAI()
p = 'X'


def start_turn(myboard):
    board.update_board(myboard)
    p = 'X'
    print(p + " your move")
    #userInput(p,spot)
    if board.check_score():
        print(p + " is the winner")
        moves = False
    if not board.check_moves_available() and moves!=False:
        print ("It's a tie!")
        moves = False
    p = "O"
    move = r.pickMove(board,p)
    board.make_move(move[0],move[1],p)
    if board.check_score():
        print(p + " [AI] is the winner")
        moves = False
    if not board.check_moves_available() and moves!=False:
        print ("It's a tie!")
        moves = False
    p = "X"

    print("Thank you for playing my game!!!")
    return board.return_board()



def userInput(p,spot):
        row = int(spot[0])
        column = int(spot[1])
        if board.check_space_before_input(row,column):
            board.make_move(row,column,p)
        else:
            print("try again")
