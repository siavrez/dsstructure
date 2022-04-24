
"""
Build a tic tac toe game
"""
def tictactoe(): 
    """
    Build a single player tic tac toe game 
    """
    board = [[' ' for x in range(3)] for y in range(3)]
    player = 'X'
    win = False
    tie = False
    while not win and not tie:
        print_board(board)
        print('Player ' + player + ' turn')
        move = input('Enter a move: ')
        move = move.split(',')
        move = [int(x) for x in move]
        if board[move[0]][move[1]] == ' ':
            board[move[0]][move[1]] = player
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print('Invalid move')
        win = check_win(board)
        tie = check_tie(board)
    print_board(board)
    if win:
        print('Player ' + player + ' wins!')
    else:
        print('Tie!')

def print_board(board):
    """ 
    Print the board
    """
    for row in board:
        print(row)
        
def check_win(board):

    """
    Check if there is a win
    """
    win = False
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            win = True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            win = True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        win = True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        win = True
    return win

def check_tie(board):
    """
    Check if there is a tie
    """
    tie = False
    for row in board:
        for col in row:
            if col == ' ':
                tie = False
    return tie
if __name__ == "__main__":
    tictactoe()