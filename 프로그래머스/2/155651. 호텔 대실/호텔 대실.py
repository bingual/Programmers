from collections import defaultdict


def solution(book_time):
    room = defaultdict(int)
    for i, time in enumerate(sorted(book_time)):
        start = convert(time[0])
        end = convert(time[1])

        assigned = False
        for j, check_out in room.items():
            if check_out <= start:
                room[j] = end + 10
                assigned = True
                break

        if not assigned:
            room[i] = end + 10

    return len(room)


def convert(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)