def rod_cutting(i,N,val,dp):
    if i == 0:
        return N*val[0]
    if dp[i][N] != -1:
        return dp[i][N]
    not_cut = rod_cutting(i-1,N,val,dp)
    cut = -1e9
    rod_length = i + 1
    if rod_length <= N:
        cut = rod_cutting(i,N-rod_length,val,dp) + val[i]
    dp[i][N] = max(not_cut,cut)
    return dp[i][N]
price = [2, 5, 7, 8, 10]
n = len(price)
dp = [[-1]*(n+1) for i in range(n)]
print(rod_cutting(n-1,n,price,dp))

def rod_cutting_t(N,val):
    dp = [[0]*(n+1) for i in range(n)]
    for i in range(n+1):
        dp[0][i] = i*val[0]
    for i in range(1,n):
        for j in range(n+1):
            not_pick = dp[i-1][j]
            pick = -1e9
            rod_length = i + 1
            if rod_length <= j:
                pick = val[i] + dp[i][j-rod_length]
            dp[i][j] = max(pick,not_pick)
    return dp[n-1][n]
print(rod_cutting_t(len(price),price))
