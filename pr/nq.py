def solve_n_queens(n):
    board = [['.'] * n for _ in range(n)]
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        if row == n:
            for r in board:
                print(''.join(r))
            return True  # stop after first solution

        for c in range(n):
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue

            board[row][c] = 'Q'
            cols.add(c)
            diag1.add(row - c)
            diag2.add(row + c)

            if backtrack(row + 1):
                return True  # early stop after first solution

            board[row][c] = '.'
            cols.remove(c)
            diag1.remove(row - c)
            diag2.remove(row + c)

        return False  # no valid position in this row

    backtrack(0)

# Example usage
solve_n_queens(8)