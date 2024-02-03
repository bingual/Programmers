def solution(s):
    if s[0] == ")" or s[-1] == "(":
        return False

    if len(s) % 2 != 0:
        return False

    stack = []
    cnt = 0
    for char in s:
        stack.append(char)
        if len(stack) >= 2 and stack[-2] + stack[-1] == "()":
            del stack[-1]
            del stack[-1]
            cnt += 1

    if cnt != len(s) // 2:
        return False
    return True