from collections import defaultdict


def solution(name, yearning, photo):
    answer = []
    # name:yearning 딕셔너리 생성
    combos = defaultdict(int, {a: b for a, b in zip(name, yearning)})

    # photo[i][j] == name[j] 라면 yearning[j] * n 만큼 answer에 저장
    for a in photo:
        total = 0
        for b in a:
            total += combos[b]
        answer.append(total)

    return answer