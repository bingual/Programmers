def solution(files):
    hnt = []
    for i, file in enumerate(files):
        state = [False] * 2
        h, n, t = "", "", ""
        for char in file:
            if not char.isdigit() and not state[0]:
                h += char
            if char.isdigit() and not state[1]:
                state[0] = True
                n += char
            elif state[0]:
                state[1] = True
                t += char
        hnt.append((h, n, t))

    sort = sorted(
        hnt,
        key=lambda x: (
            x[0].lower(),
            int(x[1]),
        ),
    )

    return ["".join([h, n, t]) for h, n, t in sort]