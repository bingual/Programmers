def solution(s, n):
    answer = []

    for c in s:
        if c.isalpha():
            # 알파벳 총 개수는 26, 문자가 b이상 n이 25이상 이라면 밀엇을 때 알파벳 유니코드 범위를 벗어 나기에 등차 적용후 밀기
            standard = ord("a") if c.islower() else ord("A")  # 문자가 소문자, 대문자 인지로 기준 설정
            # s='a', n=25 -> (97 - 97 + 25) % 26 + 97 = 122 -> 'z'
            shift = chr((ord(c) - standard + n) % 26 + standard)
            answer.append(shift)
        else:
            answer.append(c)

    return "".join(answer)