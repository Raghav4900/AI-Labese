def is_safe(board, row, col):
    # Check column and diagonals for all previous rows
    for r in range(row):
        if board[r] == col:                        # same column
            return False
        if abs(board[r] - col) == abs(r - row):   # same diagonal
            return False
    return True

def solve_nqueens(n, row, board, solutions):
    if row == n:                          # all queens placed!
        solutions.append(board[:])        # save a copy
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col              # place queen
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1              # backtrack (remove queen)

def print_board(solution, n):
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)
    print()

n = int(input("Enter N for N-Queens: "))
solutions = []
solve_nqueens(n, 0, [-1] * n, solutions)

print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
for i, sol in enumerate(solutions):
    print(f"Solution {i+1}: {sol}")
    print_board(sol, n)