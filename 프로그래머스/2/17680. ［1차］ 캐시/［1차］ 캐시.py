from collections import deque


def solution(cacheSize, cities):
    answer = 0

    cities = list(map(str.lower, cities))
    cache = deque(maxlen=cacheSize)
    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5

        cache.append(city)

    return answer