from collections import deque


def solution(s):
    stack = deque()
    for char in s:
        stack.append(char)

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    answer = 0 if stack else 1

    return answer