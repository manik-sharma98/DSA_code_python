def knap(i,W,val,weights,dp):
    if i == 0:
        if weights[0] <= W:
            return (W//weights[0]) * val[0]
        return 0
    if dp[i][W] != -1:
        return dp[i][W]
    not_pick = 0 + knap(i-1,W,val,weights,dp)
    pick = -1e9
    if weights[i] <= W:
        pick = val[i] + knap(i,W-weights[i],val,weights,dp)
    dp[i][W] = max(pick,not_pick)
    return dp[i][W]
wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
n = len(wt)
dp = [[-1]*(W+1) for i in range(n)]
print(knap(n-1,W,val,wt,dp))

def knap_t(W,val,weights):
    n = len(weights)
    dp = [[0]*(W+1) for i in range(n)]
    
    for i in range(weights[0],W+1):
        dp[0][i] = (i//weights[0]) * val[0]
    
    for i in range(1,n):
        for j in range(W+1):
            not_pick = dp[i-1][j]
            pick = -1e9
            if weights[i] <= j:
                pick = dp[i][j-weights[i]] + val[i]
            dp[i][j] = max(pick,not_pick)
    return dp[n-1][W]
print(knap_t(W,val,wt))