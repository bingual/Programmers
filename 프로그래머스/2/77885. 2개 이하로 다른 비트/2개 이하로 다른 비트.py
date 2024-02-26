def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(((num ^ (num + 1)) >> 2) + num + 1)
    return answer