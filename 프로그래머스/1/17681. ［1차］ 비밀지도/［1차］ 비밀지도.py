def solution(n, arr1, arr2):
    answer = []
    # 공백으로 이루어진 전체맵
    maps = [[" " for _ in range(n)] for _ in range(n)]

    for i in range(n):
        # 맵을 순회 하면서 십진수 -> 이진수 변환
        m1 = bin(arr1[i])[2:].rjust(n, "0")
        m2 = bin(arr2[i])[2:].rjust(n, "0")

        # 벽을 #으로 변환
        for j in range(n):
            if m1[j] == "1" or m2[j] == "1":
                maps[i][j] = "#"

        # 출력 결과에 맞게 삽입
        answer.append("".join(maps[i]))

    return answer