from collections import deque 


def solution(order):
    answer = 0
    
    order = deque(order)
    sub = deque()
    for i in range(len(order)):
        main = i + 1
        if main == order[0]:
            order.popleft()
            answer += 1
        else:
            sub.append(main)
            
        if sub and sub[-1] == order[0]:
            order.popleft()
            sub.pop()
            answer += 1
            
    while sub and sub[-1] == order[0]:
        order.popleft()
        sub.pop()
        answer += 1
        
    return answer