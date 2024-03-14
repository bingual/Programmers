from itertools import permutations
import re


def solution(expression):
    answer = 0
    numbers = list(map(int, re.split("[*+-]", expression)))
    operators = re.findall("[*+-]", expression)

    for operator_order in permutations(["*", "+", "-"]):
        temp_numbers = numbers[:]
        temp_operators = operators[:]

        for op in operator_order:
            i = 0
            while i < len(temp_operators):
                if temp_operators[i] == op:
                    if op == "+":
                        temp_numbers[i] += temp_numbers[i + 1]
                    elif op == "-":
                        temp_numbers[i] -= temp_numbers[i + 1]
                    elif op == "*":
                        temp_numbers[i] *= temp_numbers[i + 1]

                    del temp_numbers[i + 1]
                    del temp_operators[i]
                else:
                    i += 1

        answer = max(answer, abs(temp_numbers[0]))
    return answer
