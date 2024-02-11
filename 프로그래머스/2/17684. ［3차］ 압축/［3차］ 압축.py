def solution(msg):
    answer = []

    dicts = {chr(64 + i): i for i in range(1, 27)}
    n = len(msg)
    i = 0
    while i < n:
        w = msg[i]
        while i + 1 < n and w + msg[i + 1] in dicts:
            i += 1
            w += msg[i]

        answer.append(dicts[w])
        if i + 1 < n:
            dicts[w + msg[i + 1]] = len(dicts) + 1
        i += 1
        
    return answer