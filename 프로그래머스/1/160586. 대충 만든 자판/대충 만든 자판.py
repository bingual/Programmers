def solution(keymap, targets):
    answer = []

    for target in targets:
        total = 0
        for t_char in target:
            temp = 101
            for key in keymap:
                # 문자가 keymap[i]에 포함 돼있을 때 해당 문자의 인덱스 최소 값 파싱
                if t_char in key:
                    temp = min(temp, key.index(t_char) + 1)
            # 문자가 존재 한다면 값을 더함
            if temp < 101:
                total += temp
            # 문자가 존재 하지 않다면 -1
            else:
                total = -1
                break
        # 결과 값 삽입
        answer.append(total)

    return answer