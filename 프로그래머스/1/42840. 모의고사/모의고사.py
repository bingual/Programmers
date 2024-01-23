def solution(answers):
    # 각 수포자 패턴 선언
    pattern1 = [
        1,
        2,
        3,
        4,
        5,
    ]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [
        3,
        3,
        1,
        1,
        2,
        2,
        4,
        4,
        5,
        5,
    ]
    cnt = [0, 0, 0]  # 각 수포자 정답 개수 카운트
    for i, item in enumerate(answers):
        if item == pattern1[i % len(pattern1)]:
            cnt[0] += 1
        if item == pattern2[i % len(pattern2)]:
            cnt[1] += 1
        if item == pattern3[i % len(pattern3)]:
            cnt[2] += 1

    #  가장 높은 점수를 받은 사람 특정
    answer = [i + 1 for i, item in enumerate(cnt) if item == max(cnt)]
    return answer