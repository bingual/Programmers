from functools import lru_cache
import sys

sys.setrecursionlimit(10000000)


@lru_cache(maxsize=None)
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (solution(n - 1) + solution(n - 2)) % 1234567
