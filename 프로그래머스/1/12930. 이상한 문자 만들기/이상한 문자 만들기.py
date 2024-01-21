def solution(s):
    words = s.split(" ")
    result = []

    for word in words:
        converted_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                converted_word += word[i].upper()
            else:
                converted_word += word[i].lower()
        result.append(converted_word)

    return " ".join(result)