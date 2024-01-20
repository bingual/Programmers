def solution(n, computers):
    answer = 0
    visited = [0 for _ in computers]  # 생성 가능한 네트워크 개수 만큼 생성

    def dfs(i):
        # 현재 경로에 네트워크 생성
        visited[i] = 1

        # 다음 경로에 네트워크가 생성 되어 있지 않고 컴퓨터가 연결 되어있다면 재귀 호출
        for j in range(n):
            if not visited[j] and computers[i][j]:
                dfs(j)

    for i in range(n):
        if not visited[i]:  # 네트워크가 생성 되어 있지 않다면 함수 호출
            dfs(i)
            answer += 1  # 연결된 네트워크 카운트

    return answer