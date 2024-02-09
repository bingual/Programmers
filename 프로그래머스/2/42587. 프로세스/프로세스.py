from collections import deque


def solution(priorities, location):
    process = {i: priority for i, priority in enumerate(priorities)}
    que = deque(process.items())

    sorted_key = []
    while que:
        priority = max(que, key=lambda x: x[1])[1]
        key, value = que.popleft()

        if value < priority:
            que.append((key, value))
        else:
            sorted_key.append(key)

    return sorted_key.index(location) + 1