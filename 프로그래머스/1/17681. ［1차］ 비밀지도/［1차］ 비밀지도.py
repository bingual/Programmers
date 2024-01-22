def solution(n, arr1, arr2):
    maps = [[" " for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m1 = bin(arr1[i]).replace("0b", "", 1).rjust(n, "0")
        m2 = bin(arr2[i]).replace("0b", "", 1).rjust(n, "0")

        for j in range(n):
            if m1[j] == "1" or m2[j] == "1":
                maps[i][j] = "#"

    answer = ["".join(a) for a in maps]
    return answer