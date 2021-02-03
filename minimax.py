import random
from math import inf as infinity

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "],]

def print_board():
    print('-------------')
    for row in board:
        print("  |  ".join(row))
        print('-------------')

def check_game_over(board):
    for row in range(len(board)):
        if board[0][row] == board[1][row] == board[2][row] == "X":
            return "X"
        elif board[0][row] == board[1][row] == board[2][row] == "O":
            return "O"

    for col in range(len(board[0])):
        if board[col][0] == board[col][1] == board[col][2] == "X":
            return "X"
        elif board[col][0] == board[col][1] == board[col][2] == "O":
            return "O"

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X" : return "X"
        elif board[0][0] == "O" : return "O"
    
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X" : return "X"
        elif board[0][2] == "O" : return "O"

    for row in board:
        for col in row:
            if col == " ":
                return "C"
    return "N"

scores = {'X' : 1, 'O' : -1, 'N' : 0}

def minimax(board, isMax, depth = 1):
    result = check_game_over(board)
    if result != "C":
        return scores[result]
    if isMax:
        best_score = -2
        for row in range(3):
            for col in range(3):
                if board[col][row] == " ":
                    board[col][row] = "X"
                    score = minimax(board, False, depth+1)
                    board[col][row] = " "
                    best_score = max(score, best_score)
    else:
        best_score = 2
        for row in range(3):
            for col in range(3):
                if board[col][row] == " ":
                    board[col][row] = "O"
                    score = minimax(board, True, depth+1)
                    board[col][row] = " "
                    best_score = min(score, best_score)

    return best_score
            
def bestMove(board, turn):
    bestCol = bestRow = -1
    bestScore = -2
    for row in range(3):
        for col in range(3):
            if board[col][row] == " ":
                board[col][row] = "X"
                score = minimax(board, turn)
                board[col][row] = " "
                if score > bestScore:
                    bestScore = score 
                    bestCol = col
                    bestRow = row
    print(bestScore)
    return bestCol, bestRow

turn = False

inp = input("ENTER 1 IF YOU WANNA START FIRST.. ELSE ENTER 0 : ")

def isValid(row, col):
    if row > 3 or row < 0 or col > 3 or col < 0:
        print("INVALID _")
        return False
    if board[col][row] != " ":
        print("INVALID")
        return False
    return True

def take_input():
    row = int(input("Enter col : "))-1
    col = int(input("Enter row : "))-1
    if isValid(row, col):
        board[col][row] = "O"
    else:
        take_input()

def make_move(row, col):
    board[col][row] = "X"
        
if inp == "0":
    turn = not turn

while check_game_over(board) == "C":
    if turn:
        print("my turn..")
        col, row = bestMove(board, not turn)
        print(row, col)
        make_move(row, col)
    else :
        print("ur turn...")
        take_input()
    print_board()
    turn = not turn

print(check_game_over(board) + " won the game")