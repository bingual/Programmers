def solution(number, limit, power):
    answer = 0
    cnt = divisors(number)  # 모든 숫자에 대한 약수 개수 미리 계산

    for i in range(1, number + 1):
        temp = cnt[i]
        if temp > limit:
            answer += power
        else:
            answer += temp

    return answer


def divisors(n):
    total = [0] * (n + 1)
    for i in range(1, int(n**0.5) + 1):
        for j in range(i * i, n + 1, i):  # i의 배수들에 대해 약수 개수를 증가
            total[j] += 2 if i * i != j else 1
    return total