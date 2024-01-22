from datetime import datetime


def solution(a, b):
    date = datetime(2016, a, b)
    answer = date.strftime("%A")[:3].upper()
    return answer