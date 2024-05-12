N = 8

def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, count):
    # Base case: If all queens are placed, return True
    if col >= N:
        count[0] += 1
        print_solution(board)
        return True

    # Place this queen in board[i][col]
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_n_queens(board, col + 1, count)

            # If placing queen in board[i][col] doesn't lead to a solution, remove the queen
            board[i][col] = 0

    # If the queen can not be placed in any row in this column, return False
    return False

def solve_nq():
    board = [[0 for j in range(N)] for i in range(N)]
    count = [0]
    solve_n_queens(board, 0, count)
    print(f"Number of solutions: {count[0]}")

def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

# Driver code
solve_nq()
