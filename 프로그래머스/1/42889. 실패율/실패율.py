from collections import Counter
from functools import cmp_to_key


def solution(N, stages):
    stage = Counter(stages)  # 분자
    m = len(stages)  # 분모

    # 실패율 구하기
    failure = {}
    for i in range(1, N + 1):
        m -= stage[i - 1]
        if m != 0:
            failure[i] = stage[i] / m
        else:
            failure[i] = 0

    # 실패율 기준 내림차 정렬
    sorted_failure = sorted(failure.items(), key=cmp_to_key(cmp))

    # 출력 결과에 맞게 변환
    answer = [item[0] for item in sorted_failure]
    return answer


def cmp(x, y):
    return y[1] - x[1]