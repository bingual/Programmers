def solution(park, routes):
    n, m = len(park), len(park[0])

    # 방향 설정
    direction = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1),
    }

    def search(y, x):
        for route in routes:
            key, value = route.split()  # 방향, 거리

            dy, dx = direction[key]  # key로 방향 특정
            ty, tx = y, x  # 현재 좌표 초기화

            for _ in range(int(value)):
                ny, nx = ty + dy, tx + dx  # 이동할 방향

                if 0 <= ny < n and 0 <= nx < m and park[ny][nx] != "X":
                    # 벽을 넘어가지 않았고 X를 만나지 않았다면 현재 좌표 저장
                    ty, tx = ny, nx
                else:
                    ty, tx = y, x  # 현재 좌표 초기화
                    break
            # 이동 결과
            y, x = ty, tx
        return y, x

    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                return list(search(i, j))