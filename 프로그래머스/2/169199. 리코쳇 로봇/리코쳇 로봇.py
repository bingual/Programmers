from collections import deque


def solution(board):
    n, m = len(board), len(board[0])
    board = [list(word) for word in board]

    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        board[x][y] = "V"

        que = deque()
        que.append((x, y, 0))
        while que:
            x, y, c = que.popleft()
            if board[x][y] == "G":
                return c

            for i in range(4):
                tx, ty = x, y
                while True:
                    nx, ny = tx + dx[i], ty + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "D":
                        tx, ty = nx, ny
                    else:
                        if board[tx][ty] != "V":
                            que.append((tx, ty, c + 1))

                        if board[tx][ty] != "G":
                            board[tx][ty] = "V"
                        break
        return -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                return bfs(i, j)