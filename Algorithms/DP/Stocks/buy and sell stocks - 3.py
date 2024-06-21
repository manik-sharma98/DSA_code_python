def maxProfitKTransactions(k, prices):
    n = len(prices)
    dp = [[0] * (2 * k + 1) for _ in range(n)]

    for trans in range(1, 2 * k, 2):
        dp[-1][trans] = -prices[-1]

    for i in range(n - 2, -1, -1):
        for trans in range(2 * k - 1, -1, -1):
            if trans % 2 == 0:
                dp[i][trans] = max(-prices[i] + dp[i + 1][trans + 1], dp[i + 1][trans])
            else:
                dp[i][trans] = max(prices[i] + dp[i + 1][trans + 1], dp[i + 1][trans])

    return dp[0][0]

# Example usage:
k = 2
prices = [7, 1, 5, 3, 6, 4]
print(maxProfitKTransactions(k, prices))
