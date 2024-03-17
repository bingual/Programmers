def solution(rows, columns, queries):
    answer = []
    board = [[(j + 1) + (i * columns) for j in range(columns)] for i in range(rows)]
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        copy_board = [row[:] for row in board]
        min_values = []
        # top
        board[x1][y1] = copy_board[x1 + 1][y1]
        min_values.append(board[x1][y1])
        for i in range(y1 + 1, y2 + 1):
            board[x1][i] = copy_board[x1][i - 1]
            min_values.append(board[x1][i])
        # right
        for i in range(x1 + 1, x2 + 1):
            board[i][y2] = copy_board[i - 1][y2]
            min_values.append(board[i][y2])
        # bottom
        for i in range(y1, y2):
            board[x2][i] = copy_board[x2][i + 1]
            min_values.append(board[x2][i])
        # left
        for i in range(x1 + 1, x2):
            board[i][y1] = copy_board[i + 1][y1]
            min_values.append(board[i][y1])
        answer.append(min(min_values))
    return answer