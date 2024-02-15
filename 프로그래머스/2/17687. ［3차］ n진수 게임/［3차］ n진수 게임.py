def solution(n, t, m, p):
    answer = []
    decimals = []

    i = 0
    while len(decimals) < t * m:
        decimals.extend(convert(i, n))
        i += 1

    for i in range(t):
        answer.append(decimals[p - 1 + i * m])
    print(answer)

    return "".join(answer)


def convert(n, b):
    if n == 0:
        return ["0"]

    decimals = []
    while n > 0:
        r = n % b
        decimals.append(str(r) if r < 10 else chr(65 + r - 10))
        n //= b

    return decimals[::-1]