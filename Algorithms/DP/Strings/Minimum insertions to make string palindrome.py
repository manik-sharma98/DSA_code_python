def min_insert(s1,s2,i,j,dp):
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = 1+min_insert(s1,s2,i-1,j-1,dp)
    else:
        dp[i][j] = max(min_insert(s1,s2,i-1,j,dp),min_insert(s1,s2,i,j-1,dp))

    return dp[i][j]
s1 = 'abcaa'
s2 = s1[::-1]
n = len(s1)
m = len(s2)
dp = [[-1]*(m+1) for i in range(n+1)]
lcs = min_insert(s1,s2,n-1,m-1,dp)
print(n-lcs)

def min_insert_t(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+1) for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]
lcs_t = min_insert_t(s1,s1[::-1])
print(n-lcs_t)
