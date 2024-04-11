import heapq


def solution(book_time):
    heap = []
    for start, end in sorted(book_time):
        start, end = convert(start), convert(end)
        clean = end + 10
        if heap and start >= heap[0]:
            p = heapq.heappop(heap)           
            heapq.heappush(heap, (clean))
        else:
            heapq.heappush(heap, (clean))
    return len(heap)


def convert(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)