from fractions import Fraction
from collections import defaultdict
from functools import cmp_to_key


def solution(N, stages):
    mol = defaultdict(int)
    den = {}

    # 분자 구하기
    for i, item in enumerate(stages):
        mol[item] += 1

    # 분모 구하기
    temp = len(stages)
    for i in range(N):
        temp -= mol[i + 1]
        den[i + 1] = temp

    # 실패율 구하기
    failure = {}
    for i in range(1, N + 1):
        # 한 스테이지에서 전원 실패일 경우 분모가 0이면 0으로 나눌 수 가 없기에 분자를 값으로 넣어줌
        if den[i] != 0:
            failure[i] = Fraction(mol[i], den[i])
        else:
            failure[i] = mol[i]

    # 실패율 기준 내림차 정렬
    sorted_failure = sorted(failure.items(), key=cmp_to_key(cmp), reverse=True)

    # 출력 결과에 맞게 변환
    answer = [item[0] for item in sorted_failure]
    return answer


def cmp(x, y):
    return x[1] - y[1]