import re


def solution(files):
    d = re.compile(r"\d+")
    return sorted(files, key=lambda x: (re.split(d, x)[0].lower(), int(re.findall(d, x)[0])))
