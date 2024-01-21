def solution(strings, n):
    def sort(string):
        return (string[n], string)

    answer = sorted(strings, key=sort)

    return answer