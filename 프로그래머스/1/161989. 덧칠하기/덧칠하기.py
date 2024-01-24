def solution(n, m, section):
    answer = 0
    n = 0
    # 페인트를 칠해야 하는 영역이 페인트를 칠한 영역보다 크다면
    # section[i] 부터 section[i] + m - 1 까지 페인트질하고 현재 값 저장하고 카운트
    for item in section:
        if n < item:
            n = item + m - 1
            answer += 1

    return answer
