def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)

    comb = []
    for i in range(0, len(score), m):
        temp = score[i : m + i]
        if len(temp) == m:
            comb.append(temp)

    for a in comb:
        answer += min(a) * len(a)

    return answer