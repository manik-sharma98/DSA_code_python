def lcs(s1,s2,i,j,count,dp):
    if i == 0 or j == 0:
        return count
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i-1] == s2[j-1]:
        count = lcs(s1,s2,i-1,j-1,count+1,dp)
    else:
        count = max(count,max(lcs(s1,s2,i-1,j,0,dp),lcs(s1,s2,i,j-1,0,dp)))
    dp[i][j] = count
    return dp[i][j]

s1 = "abcjklp"
s2 = "acjkp"
n = len(s1)
m = len(s2)
dp = [[-1]*(m+1) for i in range(n+1)]
print(lcs(s1,s2,n-1,m-1,0,dp))

def lcs_t(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1]*(m+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1,m+1):
        dp[0][i] = 0
    
    ans = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                val = 1 + dp[i-1][j-1]
                dp[i][j] = val
                ans = max(val,ans)
            else:
                dp[i][j] = 0
    return ans
print(lcs_t(s1,s2))