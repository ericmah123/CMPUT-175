# ----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: 
# Collaborators:
# References:
# ----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3  # number of columns and rows of board

        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)

    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           



        horizo_line = '-------------'



        def entryToStr(entry:int):
            if entry == 0:
                return ' '
            else:
                return entry



        l1 = print('{0:>4d} {1:>4d} {2:>4d}'.format(0, 1, 2))
        l2 = print('0  {} |  {}  | {}  '.format(entryToStr(self.board[0][0]), entryToStr(self.board[0][1]), entryToStr(self.board[0][2])))
        l3 = print('{0:>14}'.format(horizo_line))
        l4 = print('1  {} |  {}  | {}  '.format(entryToStr(self.board[1][0]), entryToStr(self.board[1][1]), entryToStr(self.board[1][2])))
        l5 = print('{0:>14}'.format(horizo_line))
        l6 = print('2  {} |  {}  | {}  '.format(entryToStr(self.board[2][0]), entryToStr(self.board[2][1]), entryToStr(self.board[2][2])))


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        # TO DO: delete pass and complete method
        if self.board[row][col] > 0:
            return False
        else:
            return True

    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        # TO DO: delete pass and complete method

        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True
        else:
            return False


    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        # TO DO: delete pass and complete method

        check = True
        for sublist in self.board:
            for individual_num in sublist:
                if individual_num == 0:
                    return False
                else:
                    check = True

        return check






    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # TO DO: delete pass and complete method

        if (self.board[0][0] + self.board[1][1] + self.board[2][2] == 15) or (self.board[0][2] + self.board[1][1] + self.board[2][0] == 15) or \
                (self.board[0][0] + self.board[0][1] + self.board[0][2] == 15) or (self.board[1][0] + self.board[1][1] + self.board[1][2] == 15) or (self.board[2][0] + self.board[2][1] + self.board[2][2] == 15) or \
                (self.board[0][0] + self.board[1][0] + self.board[2][0] == 15) or (self.board[0][1] + self.board[1][1] + self.board[2][1] == 15) or (self.board[0][2] + self.board[1][2] + self.board[2][2] == 15):
            return True
        else:
            return False



if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required

    # start by creating empty board and checking the contents of the board attribute

    myBoard = NumTicTacToe()
    # print('Contents of board attribute when object first created:')
    # print(myBoard.board)

    # does the empty board display properly?

    # myBoard.drawBoard()


    # assign a number to an empty square and display




    myBoard.update(0, 0, 0)
    myBoard.update(0, 1, 0)
    myBoard.update(0, 2, 5)
    myBoard.update(1, 0, 0)
    myBoard.update(1, 1, 0)
    myBoard.update(1, 2, 5)
    myBoard.update(2, 0, 0)
    myBoard.update(2, 1, 0)
    myBoard.update(2, 2, 5)

    # print(myBoard.board)
    # myBoard.drawBoard()
    # try to assign a number to a non-empty square. What happens?

    # print(myBoard.update(0, 0, 2))

    # check if the board has a winner. Should there be a winner after only 1 entry?

    print(myBoard.boardFull())
    myBoard.drawBoard()

    # check if the board is full. Should it be full after only 1 entry?


    # add values to the board so that any line adds up to 15. Display

    # check if the board has a winner

    # check if the board is full

    # write additional tests, as needed

    print(myBoard.isWinner())
