from itertools import combinations


def solution(nums):
    answer = 0
    for item in combinations(nums, 3):
        divisors = []
        sum_comb = sum(item)
        for i in range(1, sum_comb + 1):
            if sum_comb % i == 0:
                divisors.append(i)
        if len(divisors) == 2:
            answer += 1

    return answer