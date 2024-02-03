import sys

sys.setrecursionlimit(10000000)


def solution(n):
    memo = {}

    def recursion(prev, current, cnt):
        if cnt == n:
            return current % 1234567

        if (prev, current, cnt) in memo:
            return memo[(prev, current)]

        temp = recursion(current, prev + current, cnt + 1)
        memo[(prev, current)] = temp

        return temp

    answer = recursion(1, 1, 2)
    return answer