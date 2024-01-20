from collections import deque


def solution(begin, target, words):
    answer = 0
    max_len = len(target)  # 모든 단어의 길이는 동일함

    # words에 target이 없을 시 0 반환
    if target not in words:
        return answer

    def bfs():
        que = deque()
        que.append((begin, 0))  # 바꿀 문자와 카운트 노드 삽입

        while que:
            q_begin, q_cnt = que.popleft()

            # 바꿀 문자가 목표와 동일하다면 누적 카운트 반환
            if q_begin == target:
                return q_cnt

            for word in words:
                cnt = 0
                for i in range(max_len):
                    if q_begin[i] != word[i]:
                        cnt += 1

                # 한 번에 한 개의 알파벳만 바꿀 수 있는 상태라면 노드 삽입
                if cnt == 1:
                    que.append((word, q_cnt + 1))

    answer = bfs()
    return answer