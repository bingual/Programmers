from datetime import datetime


def solution(a, b):
    date = f"2016-{a}-{b}"
    date_object = datetime.strptime(date, "%Y-%m-%d")
    day = date_object.strftime("%A")
    answer = day[:3].upper()
    return answer