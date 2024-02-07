from collections import Counter
from functools import cmp_to_key


def solution(k, tangerine):
    answer = 1
    cnt = Counter(tangerine)
    boxs = sorted(cnt.items(), key=cmp_to_key(cmp))

    kind = []
    cut = 0
    for x, y in boxs[:]:
        if y <= k:
            kind.append(x)

        cut += y
        if cut >= k:
            break

    if kind:
        answer = len(kind)

    return answer


def cmp(x, y):
    return y[1] - x[1]