from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])

    def bfs(x, y):
        # 좌표 설정
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        que = deque()
        que.append((x, y, 1))  # 현재 좌표 & 현재 좌표를 방문 처리한 카운트 노드 삽입

        while que:
            x, y, c = que.popleft()

            # 맵의 끝에 도달 했다면 누적 카운트 반환
            if x == n - 1 and y == m - 1:
                return c

            for i in range(4):
                # 다음 좌표 탐색
                nx, ny = x + dx[i], y + dy[i]

                # 다음 좌표가 맵 밖을 벗어나지 않았고 방문처리가 안됐다면 방문처리후 노드 삽입
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    que.append((nx, ny, c + 1))

        return -1

    return bfs(0, 0)