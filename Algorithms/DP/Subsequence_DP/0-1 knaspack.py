def knap(i,w,val,weights,dp):
    if i == 0:
        if weights[0] <= w:
            return val[0]
        return 0
    if dp[i][w] != -1:
        return dp[i][w]
    not_pick = 0+knap(i-1,w,val,weights,dp)
    pick = -1e9
    if weights[i] <= w:
        pick = val[i] + knap(i-1,w-weights[i],val,weights,dp)
    dp[i][w] = max(pick,not_pick)
    return dp[i][w]
wt = [1, 2, 4, 5]
val = [5, 4, 8, 6]
W = 5
n = len(wt)
dp = [[-1]*(W+1) for _ in range(n+1)]
print(knap(n-1,W,val,wt,dp))

def knap_t(val,weights,W):
    n = len(weights)
    dp = [[0]*(W+1) for _ in range(n)]
    for i in range(weights[0],W+1):
        dp[0][i] = val[0]
    
    for i in range(1,n):
        for j in range(W+1):
            not_pick = dp[i-1][j]
            pick = -1e9
            if weights[i] <= j:
                pick = dp[i-1][j-weights[i]] + val[i]
            dp[i][j] = max(pick,not_pick)
    return dp[n-1][W]
print(knap_t(val,wt,W))