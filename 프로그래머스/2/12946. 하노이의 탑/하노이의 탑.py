def solution(n):
    return dfs(n, 1, 3, 2, [])


def move(start, to, history):
    return history.append([start, to])


def dfs(n, start, to, mid, history):
    if n == 1:
        return move(start, to, history)
    else:
        dfs(n - 1, start, mid, to, history)
        move(start, to, history)
        dfs(n - 1, mid, to, start, history)
    return history