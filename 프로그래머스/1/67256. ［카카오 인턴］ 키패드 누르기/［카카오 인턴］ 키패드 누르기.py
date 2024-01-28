def solution(numbers, hand):
    answer = []
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }

    left_hand = (3, 0)  # '*'의 위치
    right_hand = (3, 2)  # '#'의 위치

    for num in numbers:
        if num in [1, 4, 7]:
            answer.append('L') 
            left_hand = keypad[num]
        elif num in [3, 6, 9]:
            answer.append('R')
            right_hand = keypad[num]
        else:
            # 맨해튼 거리 계산
            left_distance = abs(left_hand[0] - keypad[num][0]) + abs(left_hand[1] - keypad[num][1])
            right_distance = abs(right_hand[0] - keypad[num][0]) + abs(right_hand[1] - keypad[num][1])

            if left_distance < right_distance or (left_distance == right_distance and hand == "left"):
                answer.append('L')
                left_hand = keypad[num]
            else:
                answer.append('R')
                right_hand = keypad[num]

    return "".join(answer)