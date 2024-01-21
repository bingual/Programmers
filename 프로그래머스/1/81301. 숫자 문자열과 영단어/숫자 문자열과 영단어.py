def solution(s):
    t_dict1 = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    t_dict2 = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for i in range(len(t_dict1)):
        s = s.replace(t_dict1[i], str(t_dict2[t_dict1[i]]))

    answer = int(s)
    return answer