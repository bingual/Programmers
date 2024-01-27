from collections import Counter


def solution(participant, completion):
    answer = ""
    # 각 선수의 이름 해쉬화
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    # 해당 선수의 이름이 존재 하지 않다면 선수 이름 대입
    for key, value in p_counter.items():
        if value != c_counter[key]:
            answer = key

    return answer