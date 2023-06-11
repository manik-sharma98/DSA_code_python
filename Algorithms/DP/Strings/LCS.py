def lcs(s1,s2,i,j,dp):
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = 1+lcs(s1,s2,i-1,j-1,dp)
    else:
        s1_dec = lcs(s1,s2,i-1,j,dp)
        s2_dec = lcs(s1,s2,i,j-1,dp)
        dp[i][j] = max(s1_dec,s2_dec)
    return dp[i][j]

s1 = "acd"
s2 = "ced"
n = len(s1)
m = len(s2)
dp = [[-1]*(m) for i in range(n)]
print(lcs(s1,s2,n-1,m-1,dp))

def lcs_t(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+1) for i in range(n+1)] 
    for i in range(n):
        dp[i][0] = 0
    for i in range(m):
        dp[0][m] = 0
    
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n-1][m-1]
print(lcs_t(s1,s2))
