def solution(board, moves):
    answer = 0
    stack = []

    for move in moves:
        for line in board:
            # 인형이 존재 한다면 인형을 뽑고 방문 처리
            if line[move - 1] != 0:
                stack.append(line[move - 1])
                line[move - 1] = 0
                break

        # 같은 인형이 뽑혔을 때 해당수 만큼 바구니를 비우고 카운트
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            del stack[-1]
            del stack[-1]
            answer += 2

    return answer