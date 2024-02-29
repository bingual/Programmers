from collections import deque


def solution(number, k):
    que = deque()
    for num in number:
        num = int(num)
        while que and num > que[-1] and k > 0:
            que.pop()
            k -= 1
        que.append(num)
    
    while k:
        que.pop()
        k -= 1
        
    return "".join(list(map(str, que)))