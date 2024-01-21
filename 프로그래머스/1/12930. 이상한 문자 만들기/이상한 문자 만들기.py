def solution(s):
    words = s.split(" ")
    answer = []
    
    for word in words:
        converted_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                converted_word += word[i].upper()
            else:
                converted_word += word[i].lower()
        answer.append(converted_word)

    return " ".join(answer)