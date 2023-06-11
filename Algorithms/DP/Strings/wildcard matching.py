def isAllstars(s,i):
    for j in range(i+1):
        if s[j] != '*':
            return 0
    return 1

def wm(s1,s2,i,j,dp):
    if i < 0 and i < 0:
        return 1
    if i < 0 and j >= 0:
        return 0
    if j < 0 and i >= 0:
        return isAllstars(s1,i)
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j] or s1[i] == '?':
        dp[i][j] = wm(s1,s2,i-1,j-1,dp)
        return dp[i][j]
    if s1[i] == '*':
        dp[i][j] = wm(s1,s2,i-1,j,dp) or wm(s1,s2,i,j-1,dp)
        return dp[i][j]
    else:
        dp[i][j] = 0
    return dp[i][j]

s1 = "ab*cd"
s2 = "abdefcd"
n = len(s1)
m = len(s2)
dp = [[-1]*(m+1) for i in range(n+1)]
print(wm(s1,s2,n-1,m-1,dp))

def wm_t(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+1) for i in range(n+1)]
    dp[0][0] = 1

    for i in range(1,m+1):
        dp[0][i] = 0
    
    for i in range(1,n+1):
        dp[i][0] = isAllstars(s1,i)
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1] or s1[i-1]=='?':
                dp[i][j] = dp[i-1][j-1]
            else:
                if s1[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = 0
    return dp[n][m]
print(wm_t(s1,s2))