from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    
    for size in course:
        arr = []
        for order in orders:
            if len(order) < size:
                continue
            comb = combinations(sorted(order), size)
            arr.extend(comb)
        
        if not arr:
            continue
        
        cnt = Counter(arr)
        max_value = max(cnt.values())
        
        if max_value < 2:
            continue
        
        for menu, value in cnt.items():
            if value == max_value:
                answer.append("".join(menu))    
                
    answer.sort()
    return answer