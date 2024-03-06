from collections import deque


def solution(n, wires):
    answer = float("inf")
    
    def dfs(node, parent):
        nonlocal answer
        cnt = 1
        
        for item in tree[node]:
            if item != parent:
                cnt += dfs(item, node)
                
        answer = min(answer, abs(n - 2 * cnt))
        return cnt
            
    tree = {i: set() for i in range(1, n + 1)}
    for wire in wires:
        v1, v2 = wire
        tree[v1].add(v2)
        tree[v2].add(v1)
        
    dfs(1, 0)
    return answer