def solution(record):
    answer = []
    a = {}
    b = []
    for word in record:
        split = word.split()
        if len(split) > 2:
            state, uid, name = split
            a[uid] = name
            if state != 'Change':
                b.append((state, uid))
        else:
            state, uid = split
            if state != 'Change':
                b.append((state, uid))
            
    for x, y in b:
        if x == "Enter":
            answer.append(f"{a[y]}님이 들어왔습니다.")
        else:
            answer.append(f"{a[y]}님이 나갔습니다.")
        
    return answer