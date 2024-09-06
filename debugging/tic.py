#!/usr/bin/python3
def print_board(board):
    """
    Print the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there's a winner on the board.
    
    Returns:
    True if there is a winner, otherwise False.
    """
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

def is_board_full(board):
    """
    Check if the board is full and no more moves can be made.

    Returns:
    True if the board is full, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main game loop for Tic-Tac-Toe.
    Handles alternating turns between players and checks for winner or tie.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Ensure the input is within bounds
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid row or column. Please choose from 0, 1, or 2.")
                continue

            # Check if the spot is available
            if board[row][col] == " ":
                board[row][col] = player
            else:
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")
            continue

        # Check if the current player won
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
