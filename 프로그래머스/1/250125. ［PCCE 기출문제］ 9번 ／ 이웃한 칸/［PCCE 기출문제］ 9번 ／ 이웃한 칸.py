def solution(board, h, w):
    n = len(board)

    def search(y, x):
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        color = board[y][x]

        cnt = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == color:
                cnt += 1

        return cnt

    answer = search(h, w)
    return answer
