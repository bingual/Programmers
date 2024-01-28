def solution(s, skip, index):
    answer = []

    for char in s:
        # 변수 초기화
        i = 1
        shift = ord(char)
        temp = index

        # 1부터 index 만큼 문자를 넘김
        while temp > 0:
            shift = shift + 1
            # 문자가 z를 넘어갈 경우 a로 돌아감
            if shift > ord("z"):
                shift = ord("a")
            # 밀어낸 문자가 스킵에 포함 됐다면 1번 더 반복
            if chr(shift) in skip:
                temp += 1
            temp -= 1
            i += 1

        answer.append(chr(shift))

    return "".join(answer)