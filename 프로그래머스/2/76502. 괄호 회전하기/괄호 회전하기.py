from collections import deque


def solution(s):
    answer = 0

    que = deque(s)
    for _ in range(len(s)):
        if is_valid("".join(que)):
            answer += 1

        que.rotate(-1)

    return answer


def is_valid(s):
    patterns = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char in patterns.values():
            stack.append(char)
        elif char in patterns.keys():
            if not stack or stack.pop() != patterns[char]:
                return False

    return not stack