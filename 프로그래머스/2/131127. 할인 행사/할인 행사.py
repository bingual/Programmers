from collections import Counter, defaultdict


def solution(want, number, discount):
    answer = 0

    n = len(discount)
    cnt = Counter(discount)
    if not all(cnt[key] >= value for key, value in zip(want, number)):
        return answer

    for i in range(n - 9):
        temp = defaultdict(int)
        for j in range(i, i + 10):
            temp[discount[j]] += 1

        if all(temp[key] >= value for key, value in zip(want, number)):
            answer += 1

    return answer