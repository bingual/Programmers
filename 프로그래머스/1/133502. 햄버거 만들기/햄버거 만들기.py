from collections import deque


def solution(ingredient):
    answer = 0
    stack = deque()

    for item in ingredient:
        stack.append(item)

        # 빵, 야채, 고기, 빵 조합이 됐을 때 그만큼 비우고 카운트
        if len(stack) >= 4:
            if stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                for i in range(4):
                    stack.pop()
                answer += 1

    return answer