def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for line in board:
            if line[move - 1] != 0:
                stack.append(line[move - 1])
                line[move - 1] = 0
                break

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            del stack[-1]
            del stack[-1]
            answer += 2

    return answer