def solution(a, b, n):
    answer = 0

    while a <= n:
        x, y = divmod(n, a)  # 빈병으로 콜라 교환
        n = x * b + y  # 빈병 추가
        answer += x * b  # 교환한 콜라 카운트
    return answer