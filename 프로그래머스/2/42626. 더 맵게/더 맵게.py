import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        cal = min1 + (min2 * 2)
        heapq.heappush(scoville, cal)
        answer += 1

    return answer