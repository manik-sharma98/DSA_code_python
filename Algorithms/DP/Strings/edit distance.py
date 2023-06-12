def edit(s1,s2,i,j,dp):
    if i < 0:
        return j + 1
    if j < 0:
        return i + 1
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = 0 + edit(s1,s2,i-1,j-1,dp)
    else:
        dp[i][j] = 1 + min(edit(s1,s2,i-1,j,dp),edit(s1,s2,i,j-1,dp),edit(s1,s2,i-1,j-1,dp))
    return dp[i][j]

s1 = "horse"
s2 = "ros"
n = len(s1)
m = len(s2)
dp = [[-1]*(m+1) for _ in range(n+1)]
print(edit(s1,s2,n-1,m-1,dp))

def edit_t(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    
    return dp[n][m]
print(edit_t(s1,s2))