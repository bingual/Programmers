from collections import deque



def solution(maps):
    graph = [list(x) for x in maps]
    n, m = len(graph), len(graph[0])
    def bfs(x, y, end):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        graph[x][y] = "X"
        
        que = deque()
        que.append((x, y, 0))
        while que:
            x, y, c = que.popleft()
            if graph[x][y] == end:
                return c
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != "X":
                    if graph[nx][ny] != end:
                        graph[nx][ny] = "X"
                    que.append((nx, ny, c + 1))
        return -1            
    
    result1, result2, = 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "S":
                result1 = bfs(i, j, "L")
                break
                
    graph = [list(x) for x in maps]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "L":
                result2 = bfs(i, j, "E")
                break
    
    return -1 if result1 == -1 or result2 == -1 else result1 + result2