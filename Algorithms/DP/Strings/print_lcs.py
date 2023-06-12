def print_lcs(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+1) for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    i = n
    j = m
    
    str2 = ''
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            str2 += s1[i - 1] 
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    str2 = str2[::-1]
    return str2

s1 = "ABCDGH"
s2 = "AEDFHR"
print(print_lcs(s1, s2))