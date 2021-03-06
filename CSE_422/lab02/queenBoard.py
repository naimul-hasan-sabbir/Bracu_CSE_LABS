import numpy as np

#print chess board with queens as 'O' and empty positions as '-'
def printBoard(formation, queensNumber):
    board = []
    for row in range(0, queensNumber):
        array = []
        for column in range(0, queensNumber):
            if row == formation[column]:
                array.append('O')
            else:
                array.append('-')
        board.append(array)

    print("board with current formation is:")
    print(np.matrix(board))