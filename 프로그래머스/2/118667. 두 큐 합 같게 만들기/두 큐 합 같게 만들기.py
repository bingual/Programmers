from collections import deque


def solution(queue1, queue2):
    answer = 0
    
    a = deque(queue1)
    b = deque(queue2)
    cnt, a_sum, b_sum = 0, sum(a), sum(b)
    total = a_sum + b_sum
    i_sum = total // 2
    
    if total % 2 != 0:
        return -1
    
    maxsize = max(len(a), len(b)) * 3
    while a_sum != i_sum and b_sum != i_sum and a and b:
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