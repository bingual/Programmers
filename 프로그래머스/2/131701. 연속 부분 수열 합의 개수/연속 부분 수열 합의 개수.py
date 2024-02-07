def solution(elements):
    n = len(elements)
    unique = set()

    for i in range(n):
        current_sum = 0
        for j in range(n):
            current_sum += elements[(i + j) % n]
            unique.add(current_sum)

    return len(unique)