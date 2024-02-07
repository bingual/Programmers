from collections import Counter
from functools import cmp_to_key
import re


def solution(s):
    items = re.sub(r"[^0-9,]+", "", s).split(",")
    sorted_items = sorted(Counter(items).items(), key=cmp_to_key(cmp))
    answer = [int(item[0]) for item in sorted_items]

    return answer


def cmp(x, y):
    return y[1] - x[1]