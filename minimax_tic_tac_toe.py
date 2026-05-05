def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ': return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ': return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ': return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ': return board[0][2]
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return 10 - depth
    if winner == 'O': return depth - 10
    if is_full(board): return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

if __name__ == "__main__":
    board = [['X', 'O', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
    print("Best move for X:", best_move(board))
