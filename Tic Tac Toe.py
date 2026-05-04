def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]              # diagonals
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    for turn in range(9):
        print_board(board)
        print(f"\nPlayer {current_player}'s turn")
        
        while True:
            try:
                pos = int(input("Enter position (1-9): ")) - 1
                if 0 <= pos <= 8 and board[pos] == ' ':
                    break
                else:
                    print("Invalid or occupied! Try again.")
            except ValueError:
                print("Enter a number!")

        board[pos] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"\nPlayer {current_player} WINS!")
            return

        if turn == 8:
            print_board(board)
            print("\nIt's a DRAW!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()