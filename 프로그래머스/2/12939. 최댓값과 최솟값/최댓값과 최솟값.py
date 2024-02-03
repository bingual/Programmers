def solution(s):
    temp = list(map(int, s.split()))
    answer = str(min(temp)) + " " + str(max(temp))
    return answer