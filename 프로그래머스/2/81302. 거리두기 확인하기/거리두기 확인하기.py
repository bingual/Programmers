def solution(places):
    n = len(places[0])
    answer = [1] * n
    for idx, place in enumerate(places):
        out = False
        for i in range(n):
            for j in range(n):
                if place[i][j] == "P":
                    if not is_valid(place, (n, i, j)):
                        answer[idx] = 0
                        out = True
                        break
            if out:
                break
    return answer


def is_valid(place, point):
    n, x, y = point
    for i in range(x, n):
        for j in range(n):
            if x == i and y == j:
                continue
            if place[i][j] == "P":
                dist = abs(x - i) + abs(y - j)
                if dist < 2:
                    return False
                if dist == 2:
                    for k in range(min(x, i), max(x, i) + 1):
                        for l in range(min(y, j), max(y, j) + 1):
                            if x == k and y == l or i == k and j == l:
                                continue
                            if place[k][l] == "O":
                                return False
    return True