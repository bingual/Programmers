from collections import deque

def solution(bridge_length, weight, truck_weights):
    que = deque(truck_weights)
    end = deque()
    c_turn, c_weight = 0, 0
    
    while que or end:
        c_turn += 1
        if end and c_turn - end[0][1] == bridge_length:
            c_weight -= end.popleft()[0]
        
        if que and c_weight + que[0] <= weight:
            p = que.popleft()
            c_weight += p
            end.append((p, c_turn))

    return c_turn