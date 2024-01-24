def solution(s):
    answer = 0

    x_cnt, y_cnt = 0, 0
    x = ""
    for a in s:
        if not x:
            x = a

        if a == x:
            x_cnt += 1
        else:
            y_cnt += 1
        # x와 x가 아닌 다른 글자들이 나온 횟수가 같아지면 x를 초기화하고 카운트
        if x_cnt == y_cnt:
            x = ""
            answer += 1
    # 만약 두 횟수가 다른 상태에서 전부 탐색했다면 카운트
    if x_cnt != y_cnt:
        answer += 1

    return answer
