from collections import defaultdict
import heapq


def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    return sum([1 for x in dijkstra(graph, 1).values() if x <= K])


def dijkstra(graph, start):
    dists = defaultdict(lambda: float("inf"))
    dists[start] = 0
    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > dists[node]:
            continue

        for n_node, n_dist in graph[node]:
            u_dist = dist + n_dist
            if u_dist < dists[n_node]:
                dists[n_node] = u_dist
                heapq.heappush(heap, (u_dist, n_node))
    return dists