def solution(arr):
    t_dict = {i: item for i, item in enumerate(arr)}

    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            del t_dict[i - 1]

    answer = list(t_dict.values())

    return answer