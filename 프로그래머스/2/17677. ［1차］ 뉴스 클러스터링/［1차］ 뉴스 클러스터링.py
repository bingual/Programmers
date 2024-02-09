def solution(str1, str2):
    a, b = [], []

    def create_set(string, target):
        for i in range(1, len(string)):
            prev, current = string[i - 1], string[i]
            if prev.isalpha() and current.isalpha():
                temp = prev.upper() + current.upper()
                target.append(temp)

    create_set(str1, a)
    create_set(str2, b)

    inter = []
    union = []

    for item in set(a + b):
        count_a = a.count(item)
        count_b = b.count(item)
        inter.extend([item] * min(count_a, count_b))
        union.extend([item] * max(count_a, count_b))

    if not inter and not union:
        return 65536

    return int((len(inter) / len(union)) * 65536)