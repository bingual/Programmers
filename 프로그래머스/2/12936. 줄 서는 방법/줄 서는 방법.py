from math import factorial


def solution(n, k):
    answer = []
    people = [i for i in range(1, n + 1)]

    while n > 0:
        fact = factorial(n - 1)
        idx = (k - 1) // fact
        answer.append(people.pop(idx))
        k -= fact * idx
        n -= 1

    return answer