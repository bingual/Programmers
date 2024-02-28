from collections import deque


def solution(queue1, queue2):
    answer = 0

    a = deque(queue1)
    b = deque(queue2)

    a_sum, b_sum = sum(a), sum(b)
    total = a_sum + b_sum
    target = total // 2

    if total % 2 != 0:
        return -1

    maxsize = len(a) * 3
    while a_sum != target and b_sum != target:
        if maxsize <= answer:
            return -1

        if a_sum > b_sum:
            p = a.popleft()
            b.append(p)
            a_sum -= p
            b_sum += p
            answer += 1

        if b_sum > a_sum:
            p = b.popleft()
            a.append(p)
            b_sum -= p
            a_sum += p
            answer += 1

    return -1 if not a or not b else answer