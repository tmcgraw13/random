import math
from mygame.board import customBoard

class AttemptScore:
    def __init__(self, move, score) -> None:
        self.move = move
        self.score = score

class customAI:
    def __init__(self):
        self.player = ""
        self.count = 1000

    def iterateScore(self,currentScore:int):
        self.count -= 100
        return currentScore

    def pickMove(self, board:customBoard, currentPlayer:str):
        self.attempts = []
        self.finalAttempts = []
        self.scores = []
        self.player = currentPlayer
        for col in range(3):
            for row in range(3):
                if board.check_space_before_input(row, col):
                    score = self.recursion(board,currentPlayer,[row,col])
                    attempt_result = AttemptScore([row, col], score)
                    self.attempts.append(attempt_result)

        lowscore = AttemptScore([0,0], math.inf)
        for attempt in self.attempts:
            print(attempt.move,attempt.score)
            if attempt.score < lowscore.score:
                lowscore = attempt

        print('precious: ',lowscore.move, lowscore.score)
        
        return lowscore.move

    #-----------------------------------------------------#
    #                   RECURSION                         #
    #-----------------------------------------------------#
    def recursion(self, board: customBoard, currentPlayer: str, currentOption: list, counter = 10,depth=1):
        
        board2 = board.copy_board()
        # if currentPlayer != self.player:
        #     board2.find_last_winning_spot(currentPlayer)

        board2.make_move(currentOption[0],currentOption[1],currentPlayer)
        if board2.check_score():
            if currentPlayer != self.player: # player X
                extra = board2.find_last_winning_spot(currentPlayer)
                return counter+extra
            else: # player O
                if(depth == 1):
                    return -1000
                return -counter
        elif not board2.check_moves_available():
            return 0
        else:
            scores = []
            # print('I AM AT A DEPTH of ', depth)
            if currentPlayer == 'O':
                newPlayer = 'X'
            else:
                newPlayer = 'O'
            for col in range(3):
                for row in range(3):
                    if board2.check_space_before_input(row, col):
                        scores.append(self.recursion(board2,newPlayer,[row,col],counter,depth+1))

            if depth <= 1:
                print('my scores ',scores,' and my depth ', depth)
            return sum(scores)
