def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    return sum(x * y for x, y in zip(A, B))