from collections import deque


def solution(storey):
    answer = 0
    
    que = deque([int(n) for n in str(storey)])
    while que:
        p = que.pop()
        if que and p == 5 and que[-1] < 5 or not que and p == 5:
            answer += p    
        elif p >= 5:
            cal = 10 - p
            answer += cal
            
            while que and que[-1] + 1 == 10:
                que.pop()
                
            if que:
                que[-1] += 1
            elif not que:
                que.append(1)
        else:
            answer += p
    return answer