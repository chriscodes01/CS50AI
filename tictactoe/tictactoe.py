"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    
    countX = 0
    countO = 0

    for row in range(3):
        for column in range(3):
            if board[row][column] == X:
                countX += 1
            if board[row][column] == O:
                countO += 1

    if countX == countO:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """  
    possibleActions = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                possibleActions.add((row, column))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If action is not on EMTPY:
        # raise exception
    if action not in actions(board):
        raise Exception("Invalid move.")

    row, column = action
    newBoard  = copy.deepcopy(board)
    newBoard[row][column] = player(board)

    return newBoard

# All functions for checking winner
def checkRows(board, player):
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkColumns(board, player):
    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
    return False

def checkDiag1(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    return False

def checkDiag2(board, player):
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """  
    if checkRows(board, X) or checkColumns(board, X) or checkDiag1(board, X) or checkDiag2(board, X):
        return X
    elif checkRows(board, O) or checkColumns(board, O) or checkDiag1(board, O) or checkDiag2(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if winner(board) == X or winner(board) == O:
    #     return True
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(3):
        for column in range(3):    
            if board[row][column] == EMPTY:
                return False
            
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def maxValue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v

def sortMethod(x):
    return x[0]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        moves = []
        for action in actions(board):
            moves.append([minValue(result(board, action)), action])

        choiceMove = sorted(moves, key=sortMethod, reverse=True)[0][1]
        return choiceMove
    elif player(board) == O:
        moves = []
        for action in actions(board):
            moves.append([maxValue(result(board, action)), action])

        choiceMove = sorted(moves, key=sortMethod)[0][1]
        return choiceMove
