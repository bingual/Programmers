def solution(n, words):
    answer = [0, 0]

    cnt = {i: 0 for i in range(1, n + 1)}
    unique = set()
    temp = ""
    order = 1
    for i, word in enumerate(words):
        cnt[order] += 1

        # 중복된 단어 탈락 처리
        if word in unique:
            answer = [order, cnt[order]]
            break
        # 끝말잇기가 아니면 탈락 처리
        if i != 0 and temp != word[0]:
            answer = [order, cnt[order]]
            break
        # 순서 초기화
        if order == n:
            order -= order

        unique.add(word)
        temp = word[-1]
        order += 1

    return answer