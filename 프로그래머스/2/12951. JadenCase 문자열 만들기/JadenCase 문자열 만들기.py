def solution(s):
    s = s.split(" ")

    for i, word in enumerate(s):
        if word:
            s[i] = word[0].upper() + word[1:].lower()
        else:
            s[i] = word

    return " ".join(s)