def solution(n):
    answer = 0

    # 1은 소수가 아니라 0 반환
    if n < 2:
        return answer

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0, 1은 소수가 아니므로 제거

    # 제곱근 이하의 범위에서만 확인
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False  # i의 배수들을 소수에서 제외

    # 소수의 개수 반환
    answer = sum(primes)
    return answer
