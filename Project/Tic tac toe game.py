# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
    print("\n")

# Function to check if a player has won
def check_winner(board, player):
# Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([spot != ' ' for row in board for spot in row])

# Function to get a player's move
def get_player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            row, col = move // 3, move % 3
            if board[row][col] == ' ':
                return row, col
            else:
                print("That spot is already taken. Choose another one.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

# Main function to play the game
def play_game():
# Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

# Game loop
    while True:
        print(f"Player {current_player}'s turn.")
        row, col = get_player_move(board)
        board[row][col] = current_player

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    print("Game over!")

while True:
    play_game()


    '''How to play the game:
1.The board is represented by a 3x3 grid.
2.Players take turns choosing a spot on the grid, with Player 1 being 'X' and Player 2 (or the next player) being 'O'.
3.The game checks after each move if a player has won or if the game is a tie.
4.If the game is over, the winner is announced or it is declared a tie.'''
