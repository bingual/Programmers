from collections import deque


def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])
    visited = [[char for char in word] for word in maps]

    def bfs(y, x, v, t):
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        visited[y][x] = "X"

        que = deque()
        que.append((y, x, 0))

        while que:
            y, x, c = que.popleft()

            if v[y][x] == t:
                return c

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < n and 0 <= nx < m and v[ny][nx] != "X":
                    if v[ny][nx] != t:
                        v[ny][nx] = "X"
                    que.append((ny, nx, c + 1))
        return -1

    result1 = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == "S":
                result1 = bfs(i, j, visited, "L")

    visited = [[char for char in word] for word in maps]

    result2 = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == "L":
                result2 = bfs(i, j, visited, "E")

    return -1 if result1 == -1 or result2 == -1 else result1 + result2