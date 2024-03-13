from math import gcd


def solution(arrayA, arrayB):
    gcd_a, gcd_b = get_gcd(arrayA), get_gcd(arrayB)
    result1, result2 = divide(gcd_a, arrayB), divide(gcd_b, arrayA)
    if not result1 and not result2:
        return 0
    else:
        return max(gcd_a, gcd_b)


def get_gcd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result


def divide(gcd, arr):
    if gcd < 2:
        return False
    if all(n % gcd != 0 for n in arr):
        return True
    return False