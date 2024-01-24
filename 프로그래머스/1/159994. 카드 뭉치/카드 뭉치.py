def solution(cards1, cards2, goal):
    combos = []
    # cards1[i] or cards2[i] == goal[i] 라면
    # 해당 배열의 가장 첫 번째 요소를 지우고 배열에 삽입
    for a in goal:
        if a in cards1:
            pop = cards1.pop(0)
            combos.append(pop)
        if a in cards2:
            pop = cards2.pop(0)
            combos.append(pop)
    # 과정을 전부 수행 했을때 combos와 goal을 비교후 결과 반환
    answer = "Yes" if combos == goal else "No"
    return answer