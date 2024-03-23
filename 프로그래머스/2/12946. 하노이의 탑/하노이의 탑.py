def solution(n):
    return dfs(n, 1, 3, 2, [])


def dfs(n, start, to, mid, history):
    if n == 1:
        return history.append([start, to])
    else:
        dfs(n - 1, start, mid, to, history)
        history.append([start, to])
        dfs(n - 1, mid, to, start, history)
    return history