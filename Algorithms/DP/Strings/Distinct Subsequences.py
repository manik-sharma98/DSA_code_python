def ds(s1,s2,i,j,dp):
    if j < 0:
        return 1
    if i < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j]:
        leave = ds(s1,s2,i-1,j-1,dp)
        stay = ds(s1,s2,i-1,j,dp)
        dp[i][j] = leave + stay
    else:
        dp[i][j] = ds(s1,s2,i-1,j,dp)
    return dp[i][j]

s1 = "babgbag"
s2 = "bag"
n = len(s1)
m = len(s2)
dp = [[-1]*(m+1) for i in range(n+1)]
print(ds(s1,s2,n-1,m-1,dp))

def ds(s1,s2):
    n = len(s1)
    m = len(s2)

    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1,m+1):
        dp[0][i] = 0
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][m]
print(ds(s1,s2))
