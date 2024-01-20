from collections import deque


def solution(maps):
    visited = [list(item[:]) for item in maps]  # 방문 경로를 저장할 변수 선언
    n, m = len(visited), len(visited[0])

    def bfs(y, x, key, graph):
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        graph[y][x] = "X"

        que = deque()
        que.append((y, x, 0))

        while que:
            y, x, c = que.popleft()

            # 찾고자 하는 목표에 도달 했다면 탐색에 걸린 시간 반환
            if graph[y][x] == key:
                return c

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != "X":
                    # 목표가 아닐 경우 방문 처리
                    if graph[ny][nx] != key:
                        graph[ny][nx] = "X"
                    que.append((ny, nx, c + 1))
        return -1

    # 시작 위치 -> 레버 위치 탐색
    result1 = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == "S":
                result1 = bfs(i, j, "L", visited)

    visited = [list(item[:]) for item in maps]  # 방문 경로 초기화

    # 레버 위치 -> 출구 위치 탐색
    result2 = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == "L":
                result2 = bfs(i, j, "E", visited)

    # 출구나 레버에 도달할 수 없을 경우 -1 반환, 도달할 수 있다면 탐색에 걸린 시간을 합산후 반환
    answer = -1 if result1 == -1 or result2 == -1 else result1 + result2
    return answer