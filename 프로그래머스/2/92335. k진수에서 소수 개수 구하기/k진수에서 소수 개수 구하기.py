def solution(n, k):
    answer = 0

    n = list(map(int, filter(None, convert_decimal(n, k).split("0"))))

    for num in n:
        if is_primes(num):
            answer += 1

    return answer


def convert_decimal(n, k):
    result = ""
    while n > 0:
        remainder = n % k
        result = str(remainder) + result
        n //= k

    return result if result else "0"


def is_primes(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True