import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        cal = min1 + min2 * 2
        heapq.heappush(scoville, cal)
        answer += 1

    return -1 if scoville[0] < K else answer
