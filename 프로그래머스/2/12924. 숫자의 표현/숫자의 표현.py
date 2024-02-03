def solution(n):
    answer = 0
    left, right, current_sum = 1, 1, 0
    while left <= n:
        # 합이 n보다 작으면 부분합을 키움
        if current_sum < n:
            current_sum += right
            right += 1
        # 합이 n보다 크면 부분합을 줄임
        elif current_sum > n:
            current_sum -= left
            left += 1
        # 합이 n과 같으면 카운트, 새로운 부분합의 시작 위치를 탐색
        else:
            answer += 1
            current_sum -= left
            left += 1

    return answer
