from collections import defaultdict


def solution(clothes):
    answer = 1
    cdict = defaultdict(list)
    for x, y in clothes:
        cdict[y].append(x) 
    for y in cdict:
        answer *= len(cdict[y]) + 1
    return answer - 1