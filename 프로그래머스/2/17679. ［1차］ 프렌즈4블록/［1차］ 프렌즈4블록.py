from collections import deque


def solution(m, n, board):
    answer = 0

    que = deque([[char for char in item] for item in board])
    while True:
        d_set = set()
        for i in range(m):
            for j in range(n):
                p = que[i][j]

                if p == "0":
                    continue

                if (
                    i + 1 < m
                    and j + 1 < n
                    and que[i][j + 1] == p
                    and que[i + 1][j] == p
                    and que[i + 1][j + 1] == p
                ):
                    d_set.add((i, j))
                    d_set.add((i, j + 1))
                    d_set.add((i + 1, j))
                    d_set.add((i + 1, j + 1))

        if not d_set:
            break

        for i, j in sorted(d_set, key=lambda x: (x[0], x[1])):
            que[i][j] = "0"
            answer += 1

            while i > 0 and que[i - 1][j] != "0":
                que[i][j], que[i - 1][j] = que[i - 1][j], que[i][j]
                i -= 1

    return answer