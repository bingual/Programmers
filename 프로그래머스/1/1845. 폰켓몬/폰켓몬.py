def solution(nums):
    t_set = set(nums)  # 중복 번호 제거
    # 중복 번호를 제거한 배열, 기존 배열의 절반 값중 최소 값이 정답
    answer = min(len(t_set), len(nums) // 2)

    return answer