def lcs(s1,s2,n,m):
    if n == 0 or m == 0:
        return 0
    if s1[n-1] == s2[m-1]:
        return 1 + lcs(s1,s2,n-1,m-1)
    lcs_s1 = lcs(s1,s2,n-1,m)
    lcs_s2 = lcs(s1,s2,n,m-1)
    return max(lcs_s1,lcs_s2)

s1 = 'AXYZ'
s2 = 'BAZ'
print(lcs(s1,s2,4,3))

n = 1000
m = 1000
dp = [[None]*(n) for _ in range(m)]
def lcs_m(s1,s2,n,m):
    if n == 0 or m == 0:
        dp[n][m] = 0
    if dp[n][m] != None:
        return dp[n][m]
    else:
        if s1[n-1] == s2[m-1]:
            dp[n][m] = 1 + lcs(s1,s2,n-1,m-1)
        else:    
            lcs_s1 = lcs(s1,s2,n-1,m)
            lcs_s2 = lcs(s1,s2,n,m-1)
            dp[n][m] = max(lcs_s1,lcs_s2)
    return dp[n][m]
s1 = 'AXYZ'
s2 = 'BAZ'
print(lcs_m(s1,s2,4,3))

def lcs_t(s1,s2,n,m):
    dp = [[None]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]
s1 = 'AXYZ'
s2 = 'BAZ'
print(lcs_t(s1,s2,4,3))
