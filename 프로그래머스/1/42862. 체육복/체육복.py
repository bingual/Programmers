def solution(n, lost, reserve):
    lost.sort()

    # 체육복을 도난당한 학생 중 여벌 체육복이 있는 경우 빌려주기
    for item in lost[:]:
        if item in reserve:
            lost.remove(item)
            reserve.remove(item)

    # 체육복을 빌리지 못한 학생에 대해 앞번호나 뒷번호 학생에게 빌리기
    for item in lost:
        if item - 1 in reserve:
            reserve.remove(item - 1)
        elif item + 1 in reserve:
            reserve.remove(item + 1)
        else:
            n -= 1  # 체육수업을 들을 수 없는 학생 수를 감소

    return n