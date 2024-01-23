from itertools import combinations


def solution(nums):
    answer = 0
    for item in combinations(nums, 3):
        sum_comb = sum(item)
        for i in range(2, sum_comb):
            if sum_comb % i == 0:
                break
        else:
            # 1과 자신을 제외하고 나누어 떨어지면 소수가 아니니 카운트
            answer += 1

    return answer