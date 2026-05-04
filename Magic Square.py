def magic_square(n):
    # n must be odd
    square = [[0] * n for _ in range(n)]
    
    # Start at first row, middle column
    r, c = 0, n // 2
    
    for num in range(1, n * n + 1):
        square[r][c] = num
        
        # Next position: up 1, right 1
        new_r = (r - 1) % n
        new_c = (c + 1) % n
        
        # If occupied, go down instead
        if square[new_r][new_c] != 0:
            new_r = (r + 1) % n
            new_c = c
        
        r, c = new_r, new_c
    
    return square

def print_magic_square(square):
    n = len(square)
    magic_sum = n * (n * n + 1) // 2
    print(f"Magic Square of order {n}  (Magic Sum = {magic_sum})\n")
    for row in square:
        print(" ".join(f"{x:3}" for x in row))
    print()
    # Verify
    for i, row in enumerate(square):
        print(f"Row {i}: {sum(row)}")
    for j in range(n):
        print(f"Col {j}: {sum(square[i][j] for i in range(n))}")
    print(f"Diag ↘: {sum(square[i][i] for i in range(n))}")
    print(f"Diag ↗: {sum(square[i][n-1-i] for i in range(n))}")

n = int(input("Enter odd number for magic square (e.g. 3, 5): "))
result = magic_square(n)
print_magic_square(result)