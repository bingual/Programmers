from math import ceil
from collections import defaultdict


def solution(fees, records):
    history = {}
    remainder = defaultdict(int)
    fee = defaultdict(int)
    d_time, d_fee, u_time, u_fee = fees

    for item in records:
        time, num, check = item.split()
        if check == "IN":
            history[num] = convert(time)
        else:
            remainder[num] += abs(convert(time) - history[num])
            history.pop(num)

    if history:
        for num, time in history.items():
            remainder[num] += abs(time - 1439)

    for num, time in remainder.items():
        if time > d_time:
            fee[num] = d_fee + ceil((time - d_time) / u_time) * u_fee
        else:
            fee[num] = d_fee

    return [y for x, y in sorted(fee.items(), key=lambda x: x[0])]


def convert(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)