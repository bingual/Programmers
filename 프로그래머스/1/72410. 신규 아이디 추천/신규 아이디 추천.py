import re


def solution(new_id):
    new_id = new_id.lower()  # 대문자를 소문자로 치환
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)  # 소문자, 정수, -_. 외에 제거
    new_id = re.sub(r"\.{2,}", ".", new_id)  # 연속된 마침표는 하나의 마침표로 치환
    new_id = new_id.strip(".")  # 처음과 끝에 마침표 제거

    # 공백은 a로 치환
    if not new_id:
        new_id = "a"

    # 16자 이상일 때 넘어가는 문자 제거, 끝에 공백이 있다면 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")

    # 길이가 3 이상이 될 때 까지 마지막 문자를 끝에 붙임
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
