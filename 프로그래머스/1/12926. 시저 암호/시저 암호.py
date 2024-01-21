def solution(s, n):
    answer = []

    for c in s:
        if c.isalpha():
            combo = ord("a") if c.islower() else ord("A")
            shift = chr((ord(c) - combo + n) % 26 + combo)
            answer.append(shift)
        else:
            answer.append(c)

    return "".join(answer)