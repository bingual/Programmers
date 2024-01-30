from collections import defaultdict


def solution(survey, choices):
    answer = []

    # 각 지표는 이미 사전순으로 정리가 되어있음
    tables = ["RT", "CF", "JM", "AN"]
    scores = {1: 3, 2: 2, 3: 1, 5: 1, 6: 2, 7: 3}
    types = defaultdict(int)

    # 유형 점수계산
    for i in range(len(survey)):
        no, yes = survey[i][0], survey[i][1]

        if choices[i] in [1, 2, 3]:
            types[no] += scores[choices[i]]
        elif choices[i] in [5, 6, 7]:
            types[yes] += scores[choices[i]]

    # 각 지표에서 점수가 높은 순으로 정리, 점수가 같다면 사전순으로 정리
    for word in tables:
        if types[word[0]] > types[word[1]] or types[word[0]] == types[word[1]]:
            answer.append(word[0])
        else:
            answer.append(word[1])

    return "".join(answer)