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
    count = 0
    for i in range(len(board)):
        for cell in board[i]:
            if cell == X or cell == O:
                count+=1
    if count % 2 == 0:
        return X
    else:
        return O
            

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(len(board)):
        for j, cell in enumerate(board[i]):
            if cell != X and cell != O:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i , j = action

    copy_board = copy.deepcopy(board)
    if copy_board[i][j] != EMPTY:
        raise "action not valid"
    copy_board[i][j] = player(copy_board)

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O

    for row in board:
        if row == [X ,X, X]:
            return X
        if row == [O, O, O]:
            return O

    copy_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            copy_board[i][j] = board[j][i]

    for row in copy_board:
        if row == [X ,X, X]:
            return X
        if row == [O, O, O]:
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        return 0

def value(board,alpha=-2,beta=2):
    if terminal(board):
        return utility(board),None
    if player(board) == X:
        return maxvalue(board,alpha,beta)
    else:
        return minvalue(board,alpha,beta)


def maxvalue(board,alpha,beta):
    v= -2
    my_action = None
    for action in actions(board):
        minv,act = value(result(board,action),alpha,beta)
        if minv > v:
            v = minv
            my_action = action
        if(v>=beta):
            return v,my_action
        alpha = max(alpha,v)
    return v,my_action

def minvalue(board,alpha,beta):
    v = 2
    my_action = None
    for action in actions(board):
        maxv,act = value(result(board,action),alpha,beta)
        if maxv < v:
            v = maxv
            my_action = action
        if v<= alpha:
            return v,my_action
        beta = min(beta,v)

    return v,my_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return value(board)[1]