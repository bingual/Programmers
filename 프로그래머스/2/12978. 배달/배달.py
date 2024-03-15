import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def solution(N, road, K):
    graph = {x: [] for x in range(1, N + 1)}
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    distances = dijkstra(graph, 1)
    count = sum(1 for dist in distances.values() if dist <= K)
    return count