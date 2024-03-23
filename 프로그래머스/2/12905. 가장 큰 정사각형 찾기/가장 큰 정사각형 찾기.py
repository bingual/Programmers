def solution(board):
    n, m = len(board), len(board[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_val = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            max_val = max(max_val, dp[i][j])
    return max_val * max_val