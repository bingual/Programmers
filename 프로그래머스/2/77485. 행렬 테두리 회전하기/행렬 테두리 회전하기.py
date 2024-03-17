def solution(rows, columns, queries):
    answer = []
    board = [[(j + 1) + (i * columns) for j in range(columns)] for i in range(rows)]
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        min_value = float("inf")
        temp = board[x1][y1]
        min_value = min(min_value, temp)
        for i in range(x1, x2):
            board[i][y1] = board[i + 1][y1]
            min_value = min(min_value, board[i][y1])
            
        for i in range(y1, y2):
            board[x2][i] = board[x2][i + 1]
            min_value = min(min_value, board[x2][i])
            
        for i in range(x2, x1, -1):
            board[i][y2] = board[i - 1][y2]
            min_value = min(min_value, board[i][y2])
            
        for i in range(y2, y1, -1):
            board[x1][i] = board[x1][i - 1]
            min_value = min(min_value, board[x1][i])
        board[x1][y1 + 1] = temp
        answer.append(min_value)
    return answer