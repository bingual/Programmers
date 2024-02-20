# 1 2 4
#
from collections import Counter


def solution(topping):
    answer = 0
    
    a = Counter(topping)
    b = set()
    for num in topping:
        a[num] -= 1
        if a[num] <= 0:
            del a[num] 
            
        b.add(num)
        
        if len(a) == len(b):
            answer += 1     
           
    return answer