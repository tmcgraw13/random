import math
from mygame.board import customBoard

class AttemptScore:
    def __init__(self, move, score) -> None:
        self.move = move
        self.score = score

class customAI:
    def __init__(self):
        self.player = ""
        self.count = 1

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

        high = AttemptScore([0,0], -math.inf)
        print("the sum of my scores per attempt")
        for attempt in self.attempts:
            print(attempt.move,attempt.score)
            if attempt.score > high.score:
                high = attempt

        print('precious: ',high.move, high.score)
        
        return high.move

    #-----------------------------------------------------#
    #                   RECURSION                         #
    #-----------------------------------------------------#
    def recursion(self, board: customBoard, currentPlayer: str, currentOption: list, counter = 1,depth=1):
        opp = board.copy_board() # check potential winning spot for oposite player
        board2 = board.copy_board()

        board2.make_move(currentOption[0],currentOption[1],currentPlayer)
        if board2.check_score():
            if currentPlayer != self.player: # player X
                match depth:
                    case 2:
                        return -1
                    case default:
                        return 0
            else: # player O
                opp.make_move(currentOption[0],currentOption[1],currentPlayer)
                if opp.check_score(): 
                    extra = 1
                else:
                    extra = 0
                match depth:
                    case 1:
                        return 1000 + extra
                    case 3:
                        return 1 + extra
                    case 5:
                        if(currentOption == [0,0] or currentOption== [2,2]):
                            return 0
                        return 1
                    case default:
                        return 0
        elif not board2.check_moves_available():
            if depth <= 4:
                return 1
            else: return 0
        else:
            scores = []
            if currentPlayer == 'O':
                newPlayer = 'X'
            else:
                newPlayer = 'O'
            for col in range(3):
                for row in range(3):
                    if board2.check_space_before_input(row, col):
                        tally = self.recursion(board2,newPlayer,[row,col],counter,depth+1)
                        scores.append(tally)

            if depth <= 1:
                print(currentOption,'my scores ',scores,' and my depth ', depth)
            return sum(scores)
