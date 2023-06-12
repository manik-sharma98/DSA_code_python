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
    
    len_ = dp[n][m]
    i = n
    j = m
    str1 = ''
    for k in range(1,len_+1):
        str1 += '$'
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            print(i,j)
            print(s1[i - 1])
            str1 = s1[i - 1] + str1[:-1]
            i -= 1
            j -= 1
        elif s1[i - 1] > s2[j - 1]:
            i -= 1
        else:
            j -= 1
    return str1

s1 = "abcde"
s2 = "bdgek"
print(print_lcs(s1, s2))