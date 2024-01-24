def solution(k, score):
    answer = []
    temp = []

    for item in score:
        temp.append(item)
        if k < len(temp):
            temp.remove(min(temp))
        answer.append(min(temp))

    return answer
