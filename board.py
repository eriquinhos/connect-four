import numpy as np

ROW_NUMBER = 9
COL_NUMBER = 11
CONNECT = 6


# Board functions
def create_board():
    board = np.zeros((ROW_NUMBER, COL_NUMBER))
    return board


def drop_pieces(board=np.zeros((6, 7)), row=0, col=0, piece=1):
    board[row][col] = piece


def is_valid_location(board=np.zeros((6, 7)), col=0):
    return board[ROW_NUMBER - 1][col] == 0


def get_net_open_row(board=np.zeros((6, 7)), col=0):
    for i in range(ROW_NUMBER):
        if board[i][col] == 0:
            return i


def print_board(board=np.zeros((6, 7))):
    print(np.flip(board, 0))


def winning_move(board=np.zeros((6, 7)), player=1):
    # Check horizontal locations for win
    for row in range(ROW_NUMBER):
        for col in range(COL_NUMBER - (CONNECT-1)):
            if all(board[row][col + i] == player for i in range(CONNECT)):
                return True

    # Check vertical locations for win
    for row in range(ROW_NUMBER - (CONNECT-1)):
        for col in range(COL_NUMBER):
            if all(board[row + i][col] == player for i in range(CONNECT)):
                return True

    # Check positively sloped diagonals
    for row in range(ROW_NUMBER - (CONNECT-1)):
        for col in range(COL_NUMBER - (CONNECT-1)):
            if all(board[row + i][col + i] == player for i in range(CONNECT)):
                return True

    # Check negatively sloped diagonals
    for row in range(ROW_NUMBER - (CONNECT-1)):
        for col in range((CONNECT-1), COL_NUMBER):
            if all(board[row + i][col - i] == player for i in range(CONNECT)):
                return True

    return False

