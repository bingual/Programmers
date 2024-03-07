import sys
sys.setrecursionlimit(10000000)


def solution(maps):
    answer = []

    maps = [list(item) for item in maps]
    n, m = len(maps), len(maps[0])

    def dfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        cnt = int(maps[x][y])
        maps[x][y] = "X"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X":
                cnt += dfs(nx, ny)

        return cnt

    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X":
                answer.append(dfs(i, j))

    return sorted(answer) if answer else [-1]