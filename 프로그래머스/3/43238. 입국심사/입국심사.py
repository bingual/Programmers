def solution(n, times):
    answer = 0
    # 최소 시간은 1분, 최대 시간은 가장 느린 심사관이 모든 사람을 처리하는 경우
    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        total = 0

        # 각 심사대에서 처리할 수 있는 사람 수 계산
        for time in times:
            total += mid // time

        # 심사를 기다리는 사람 수가 목표치보다 작으면 시간을 늘려야 함
        if total < n:
            start = mid + 1
        # 심사를 기다리는 사람 수가 목표치보다 크면 시간을 줄여야 함
        else:
            answer = mid
            end = mid - 1

    return answer