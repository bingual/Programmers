def solution(s):
    t_dict = {
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

    for key, value in t_dict.items():
        s = s.replace(value, str(key))

    answer = int(s)
    return answer