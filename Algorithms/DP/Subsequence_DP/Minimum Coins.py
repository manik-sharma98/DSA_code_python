def coins(i,t,nums,dp):
    if i == 0:
        if t%nums[0] == 0:
            return t//nums[0]
        return int(1e9)
    if dp[i][t] != -1:
        return dp[i][t]
    not_pick = 0 + coins(i-1,t,nums,dp)
    pick = int(1e9)
    if nums[i] <= t:
        pick = 1 + coins(i,t-nums[i],nums,dp)
    dp[i][t] = min(not_pick,pick)
    return dp[i][t]

arr = [1, 2, 3]
T = 7
n = len(arr)
dp = [[-1]*(T+1) for _ in range(n)]
print(coins(len(arr)-1,T,arr,dp))

def coins_t(arr,T):
    n = len(arr)
    dp = [[0]*(T+1) for _ in range(n)]
    
    for i in range(T+1):
        if i%arr[0] == 0:
            dp[0][i] = i//arr[0]
        else:
            dp[0][i] = 1e9
    
    for i in range(1,n):
        for j in range(T+1):
            not_pick = dp[i-1][j]
            pick = 1e9
            if arr[i] <= T:
                pick = 1 + dp[i][j-arr[i]]
            dp[i][j] = min(pick,not_pick)
    return dp[n-1][T]
print(coins_t(arr,T))
