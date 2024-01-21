def solution(n):
    answer = ""

    while n > 0:
        n, rem = divmod(n, 3)
        answer += str(rem)

    return int(answer, 3)