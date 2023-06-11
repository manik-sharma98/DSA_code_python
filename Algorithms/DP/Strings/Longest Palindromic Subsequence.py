def lps(s1,s2,i,j,dp):
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = 1 + lps(s1,s2,i-1,j-1,dp)
    else:
        str1 = lps(s1,s2,i-1,j,dp)
        str2 = lps(s1,s2,i,j-1,dp)
        dp[i][j] = max(str1,str2)
    return dp[i][j]

s = "bbabcbcab"
s2 = s[::-1]
n = len(s)
m = len(s2)
dp = [[-1]*(m+1) for i in range(n+1)]
print(lps(s,s2,len(s)-1,len(s2)-1,dp))

def lps_t(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+1) for i in range(n+1)]

    for i in range(n):
        dp[i][0] = 0
    for i in range(m):
        dp[0][i] = 0
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n-1][m-1]
print(lps_t(s,s2))

