#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """Check if the board is full (draw/tie)"""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Validate input bounds
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Row and column must be 0, 1, or 2.")
                continue
            
            # Check if spot is taken
            if board[row][col] == " ":
                board[row][col] = player
                
                # Check for winner BEFORE switching players
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                
                # Check for draw
                if check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                
                # Switch players
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")
        except IndexError:
            print("Invalid input! Row and column must be 0, 1, or 2.")

tic_tac_toe()