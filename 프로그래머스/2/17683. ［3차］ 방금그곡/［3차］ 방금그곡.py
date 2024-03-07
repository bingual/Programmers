def solution(m, musicinfos):
    answer = []
    n = len(m)
    m = (
        m.replace("C#", "c")
        .replace("D#", "d")
        .replace("F#", "f")
        .replace("G#", "g")
        .replace("A#", "a")
        .replace("B#", "b")
    )

    for info in musicinfos:
        start, end, title, song = info.split(",")
        start, end = convert(start), convert(end)

        song = (
            song.replace("C#", "c")
            .replace("D#", "d")
            .replace("F#", "f")
            .replace("G#", "g")
            .replace("A#", "a")
            .replace("B#", "b")
        )

        full_song = (song * ((end - start) // len(song) + 1))[: end - start]
        if m in full_song:
            answer.append((title, end - start))

    if not answer:
        return "(None)"
    else:
        return sorted(answer, key=lambda x: (-x[1], answer))[0][0]


def convert(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)
