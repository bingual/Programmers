from collections import Counter


def solution(participant, completion):
    answer = ""
    p_counter = Counter(participant)
    c_counter = Counter(completion)

    for player in participant:
        if c_counter[player] != p_counter[player]:
            answer = player

    return answer
