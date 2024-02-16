from collections import deque

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = deque()
    
    for i in range(n):
        while stack and numbers[i] > numbers[stack[-1]]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
            
    return answer