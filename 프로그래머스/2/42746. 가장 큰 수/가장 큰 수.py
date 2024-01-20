from functools import cmp_to_key


def solution(numbers):
    # 정수값 문자열 변환후 커스텀 정렬
    sorted_str = sorted(map(str, numbers), key=cmp_to_key(cmp))
    answer = "".join(sorted_str)  # 리스트 문자열 변환
    return answer if int(answer) != 0 else "0"


def cmp(x, y):
    # 각 문자열을 더한 다음 정수로 반환해서 정렬 시행
    return int(y + x) - int(x + y)