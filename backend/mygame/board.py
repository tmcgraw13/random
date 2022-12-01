class customBoard:
    #-----------------------------------------------------------#
    #                   INITIALIZATION                          #
    #-----------------------------------------------------------#
    def __init__(self):
        #Initialize the board
        self.arrays = 3 
        self.board = [[''] * 3 for i in range(self.arrays)]

    #-----------------------------------------------------------#
    #                       Track board moves                   #
    #-----------------------------------------------------------#
    def make_move(self, row, col, play):
        # update the array with the move/play
        self.board[row][col] = play

    #-----------------------------------------------------------#
    #                       Print Board                         #
    #-----------------------------------------------------------#
    def show_board(self):

        print(self.board)
        # print a small test board
        for array in range(self.arrays):
            for val in range(self.arrays):
                print(self.board[array][val])
            print()

        # print what is currently in the "board" array
        print(self.board)

    #-----------------------------------------------------------#
    #                       Return Board Array                  #
    #-----------------------------------------------------------#
    def return_board(self):
        # retun what is currently in the "board" array
        return self.board

    #-----------------------------------------------------------#
    #                       Update Board Array                  #
    #-----------------------------------------------------------#
    def update_board(self,newBoard):
        # retun what is currently in the "board" array
        self.board = newBoard

    #-----------------------------------------------------------#
    #                       Check SCORE                         #
    #-----------------------------------------------------------#
    def check_score(self):
        if self.checkDiagonal():
            return True
        elif self.checkRows():
            return True
        elif self.checkColumns():
            return True
        else:
            #print("NO SCORE RETURNS FALSE")
            return False
            
    #                                       #
    # more functions for checking the score #
    #                                       #

    # check rows 
    def checkRows(self):
        #print("check rows")
        for row in self.board:
            if row[1] != "":
                if row[0] == row[1] == row[2]:
                    #print("winner row")
                    return True
        return False
    # check columns
    def checkColumns(self):
        #print("check columns")
        for col in range(3):
            if self.board[1][col] != "":
                if self.board[0][col] == self.board[2][col] == self.board[1][col]:
                    #print("winner column")
                    return True
        return False
    # check diagonals
    def checkDiagonal(self):
        #print("check diagonals")
        if self.board[1][1] != "":
            if self.board[1][1] == self.board[0][0] == self.board[2][2] or self.board[1][1] == self.board[0][2] == self.board[2][0]:
                #print("winner diagonal")
                return True 
        return False


    #-----------------------------------------------------------#
    #                 Check slots available                     #
    #-----------------------------------------------------------#
    def check_moves_available(self):
        for array in range(self.arrays):
            for val in range(self.arrays):
                if self.board[array][val] == "":
                    return True # yes moves are available
        return False # no moves are available

    def check_space_before_input(self,row,col):
        return self.board[row][col] == ""

    # def check_other_player_winning_spots(self,currentPlayer):
    #     if currentPlayer == 'O':
    #         newPlayer = 'X'
    #     else:
    #         newPlayer = 'O'               
        


    #-----------------------------------------------------------#
    #                 Check ai slots available and make a move  #
    #-----------------------------------------------------------#    
    # def check_moves_ai(self,p,board):
    #     self.aiboard = board
    #     for array in range(self.arrays):
    #         for val in range(self.arrays):
    #             if self.board[array][val] == "*":
    #                 return True # yes moves are available
    #     return False # no moves are available

    #-----------------------------------------------------------#
    #          Add color based on the player "X" or "O"         #
    #-----------------------------------------------------------#


#-----------------------------------------------------------#
    #          Create a copy of the board       #
    #-----------------------------------------------------------#

    def copy_board(self):
        new_board = customBoard()
        for array in range(self.arrays):
            for val in range(self.arrays):
                new_board.make_move(array,val, self.board[array][val])
        #new_board.show_board()
        return new_board




    def find_last_winning_spot(self,p):
        copy_board2 = self.copy_board()

        for col in range(3):
            for row in range(3):
                if self.check_space_before_input(row, col):
                    copy_board2.make_move(row,col,p)
                    if copy_board2.check_score():
                        return 10000
                    copy_board2 = self.copy_board()
        return 1 



