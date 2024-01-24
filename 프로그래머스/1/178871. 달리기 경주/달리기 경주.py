def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}
    player = {i: player for i, player in enumerate(players)}

    for call in callings:
        next_rank = rank[call]  # 3
        prev_name = player[next_rank - 1]  # poe
        prev_rank = rank[prev_name]  # 2

        # 순위 변경
        rank[prev_name] = next_rank
        rank[call] = prev_rank

        # 선수 변경
        player[prev_rank] = call
        player[next_rank] = prev_name

    answer = list(player.values())
    return answer