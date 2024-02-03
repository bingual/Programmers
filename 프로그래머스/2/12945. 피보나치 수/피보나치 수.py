import sys

sys.setrecursionlimit(10000000)


def solution(n):
    memo = {}

    def recursion(prev, current, cnt):
        if cnt == n:
            return current % 1234567

        # 미리 계산된 값 처리
        if (prev, current, cnt) in memo:
            return memo[(prev, current)]

        temp = recursion(current % 1234567, (prev + current) % 1234567, cnt + 1)
        memo[(prev, current)] = temp  # 계산된 값을 저장

        return temp

    return recursion(1, 1, 2)