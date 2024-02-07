def solution(progresses, speeds):
    answer = []

    while progresses:
        progresses = [progress + speed for progress, speed in zip(progresses, speeds)]

        count = 0
        while progresses and progresses[0] >= 100:
            del progresses[0]
            del speeds[0]
            count += 1

        if count > 0:
            answer.append(count)

    return answer