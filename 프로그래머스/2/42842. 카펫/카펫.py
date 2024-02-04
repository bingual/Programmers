def solution(brown, yellow):
    area = brown + yellow

    for i in range(2, int(area**0.5) + 1):
        if area % i == 0:
            width = area // i
            height = i

            if (width - 2) * (height - 2) == yellow:
                return [width, height]