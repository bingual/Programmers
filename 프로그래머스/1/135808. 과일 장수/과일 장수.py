def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)  # 사과 상자 정렬

    # 사과 상자를 각각 m 만큼 잘라서 최대 이익의 조합 생성. 남는 사과는 버림
    comb = []
    for i in range(0, len(score), m):
        temp = score[i : m + i]
        if len(temp) == m:
            comb.append(temp)

    # 총 판매 수익 계산
    for a in comb:
        answer += a[-1] * m

    return answer