from collections import Counter
import re

def solution(s):
    s = Counter(map(int, re.sub(f"[^0-9,]", "", s).split(",")))
    return [x for x, y in sorted(s.items(), key=lambda x: -x[1])]