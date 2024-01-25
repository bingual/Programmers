from collections import defaultdict


def solution(lottos, win_nums):
    zero = 0
    win = 0

    rank = defaultdict(int, {7 - i: i for i in range(1, 6)})
    rank[1] = rank[0] = 6

    for lotto in lottos:
        if lotto == 0:
            zero += 1
        if lotto in win_nums:
            win += 1

    answer = [rank[zero + win], rank[win]]
    return answer