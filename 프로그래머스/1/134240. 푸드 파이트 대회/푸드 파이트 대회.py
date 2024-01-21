def solution(food):
    answer = ["0"]

    for i in range(len(food) - 1, 0, -1):
        for j in range(food[i] // 2):
            answer.insert(0, str(i))
            answer.append(str(i))

    return "".join(answer)