from functools import cmp_to_key


def solution(data, ext, val_ext, sort_by):
    cols = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    def cmp(x, y):
        return x[cols[sort_by]] - y[cols[sort_by]]

    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑음
    for row in data[:]:
        if row[cols[ext]] > val_ext:
            data.remove(row)

    # sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
    answer = sorted(data, key=cmp_to_key(cmp))
    return answer
