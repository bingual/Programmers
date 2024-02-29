from functools import cmp_to_key

def solution(sequence, k):
    n = len(sequence)
    i_sum, end = 0, 0
    result = []
    
    for start in range(n):
        while i_sum < k and end < n:
            i_sum += sequence[end]
            end += 1
        if i_sum == k:
            result.append((start, end - 1))
        i_sum -= sequence[start]
        
    sort = sorted(result, key=lambda x: abs(x[0] - x[1]))   
    return list(sort[0])