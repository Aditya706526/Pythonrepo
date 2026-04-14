# Write code for tick-tac-toe game
import random

def greet():
    print("Good morning! Welcome to Tic Tac Toe!")
    print("You are 'X' and the computer is 'O'.")
    print("Enter your move as 'row column' (e.g., '0 1' for top middle).")

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "X":
            move = input("Enter your move (row and column): ")
            try:
                row, col = map(int, move.split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                else:
                    print("Cell already occupied. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as numbers between 0 and 2.")
                continue
        else:
            available_moves = get_available_moves(board)
            if not available_moves:
                print("It's a draw!")
                break
            move = random.choice(available_moves)
            board[move[0]][move[1]] = current_player
            print(f"Computer chose: {move[0]} {move[1]}")
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        current_player = "O" if current_player == "X" else "X"
tic_tac_toe()
