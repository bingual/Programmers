def solution(k, dungeons):
    dp = [0] * (k + 1)

    dungeons = sorted(dungeons, key=lambda x: (x[0] - x[1], x[0]))

    for dungeon in dungeons:
        min_fatigue, consume_fatigue = dungeon
        for i in range(k, min_fatigue - 1, -1):
            dp[i] = max(dp[i], dp[i - consume_fatigue] + 1)

    return dp[k]