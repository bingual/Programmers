def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}
    player = {i: player for i, player in enumerate(players)}

    for call in callings:
        temp = player[rank[call] - 1]  # poe

        # 선수 변경
        player[rank[call]] = temp
        player[rank[temp]] = call

        # 순위 변경
        rank[call] -= 1
        rank[temp] += 1

    answer = list(player.values())
    return answer