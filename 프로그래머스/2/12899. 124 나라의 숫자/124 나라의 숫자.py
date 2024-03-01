def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        r = n % 3
        answer = '124'[r] + answer
        n //= 3
    return answer