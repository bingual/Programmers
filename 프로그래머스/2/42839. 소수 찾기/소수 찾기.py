from itertools import permutations

def solution(numbers):
    answer = 0
    
    convert = []
    for i in range(1, len(numbers) + 1):
        convert.extend([int("".join(comb)) for comb in permutations(numbers, i)])
        
    for num in set(convert):
        if primes(num):
            answer += 1
    
    return answer

def primes(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True