def solve_crossword(grid, words):
    def is_valid(r, c, word, d):
        if d == 0:
            if c + len(word) > len(grid[0]): return False
            for i in range(len(word)):
                if grid[r][c+i] not in ('-', word[i]): return False
        else:
            if r + len(word) > len(grid): return False
            for i in range(len(word)):
                if grid[r+i][c] not in ('-', word[i]): return False
        return True

    def place(r, c, word, d):
        placed = []
        for i in range(len(word)):
            nr, nc = (r, c+i) if d == 0 else (r+i, c)
            if grid[nr][nc] == '-':
                grid[nr][nc] = word[i]
                placed.append((nr, nc))
        return placed

    def unplace(placed):
        for r, c in placed:
            grid[r][c] = '-'

    def solve(idx):
        if idx == len(words): return True
        word = words[idx]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                for d in (0, 1):
                    if is_valid(r, c, word, d):
                        placed = place(r, c, word, d)
                        if solve(idx + 1): return True
                        unplace(placed)
        return False

    if solve(0):
        return grid
    return None

if __name__ == "__main__":
    grid = [['-', '-', '-'], ['*', '*', '-'], ['*', '*', '-']]
    words = ['CAT', 'TO']
    res = solve_crossword(grid, words)
    if res:
        for row in res: print("".join(row))
