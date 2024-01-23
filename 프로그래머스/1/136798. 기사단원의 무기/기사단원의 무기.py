def solution(number, limit, power):
    answer = 0
    cache = {}  # 약수의 개수를 저장하는 캐시

    for i in range(1, number + 1):
        # 이미 계산한 약수의 개수가 캐시에 있는지 확인
        if i in cache:
            temp = cache[i]
        else:
            # 캐시에 없다면 약수의 개수를 계산하고 캐시에 저장
            temp = divisors(i)
            cache[i] = temp

        if temp > limit:
            answer += power
        else:
            answer += temp

    return answer


def divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # i가 n의 약수이면, n/i도 약수이므로 2를 더함
            total += 2 if i != n // i else 1

    return total
