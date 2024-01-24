def solution(wallpaper):
    n, m = len(wallpaper), len(wallpaper[0])
    start = [50, 50]
    end = [0, 0]

    # start의 x, y는 최소 값
    # end의 x, y는 최대 값 + 1 (격자형 이기 때문에 +1)
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                if start[0] > i:
                    start[0] = i
                if start[1] > j:
                    start[1] = j

                if end[0] <= i:
                    end[0] = i + 1
                if end[1] <= j:
                    end[1] = j + 1

    answer = start + end
    return answer


print(solution([".#...", "..#..", "...#."]))
