from collections import deque
import sys

sys.setrecursionlimit(10**7)


def solution(p):
    if not p or is_valid(p):
        return p

    cnt, u, v = 0, "", ""
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        elif p[i] == ")":
            cnt -= 1
        if cnt == 0:
            u, v = p[: i + 1], p[i + 1 :]
            break

    if is_valid(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse(u[1:-1])


def reverse(u):
    s = ""
    for char in u:
        if char == "(":
            s += ")"
        else:
            s += "("
    return s


def is_valid(p):
    que = deque()
    for char in p:
        if char == "(":
            que.append(char)
        else:
            if not que or que.pop() != "(":
                return False
    return not que
