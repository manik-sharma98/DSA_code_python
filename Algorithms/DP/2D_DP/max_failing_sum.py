def max_failing_sum(i,j,m,grid,dp):
    if j < 0 or j >= m:
        return float('-inf')
    if i == 0:
        return grid[0][j]
    if dp[i][j] != -1:
        return dp[i][j]
    up = grid[i][j] + max_failing_sum(i-1,j,m,grid,dp)
    leftt_diag = grid[i][j] + max_failing_sum(i-1,j-1,m,grid,dp)
    right_diag = grid[i][j] + max_failing_sum(i-1,j+1,m,grid,dp)
    dp[i][j] = max(up,leftt_diag,right_diag) 
    return dp[i][j]

def cal_untill(matrix):
    m = len(matrix[0])
    n = len(matrix)
    dp = [[-1]*m for i in range(n)]
    maxi = float('-inf')
    for j in range(m):
        ans = max_failing_sum(n-1,j,m,matrix,dp)
        maxi = max(maxi,ans)
    return maxi
matrix = [[1,2,10,4], [100,3,2,1], [1,1,20,2], [1,2,2,1]]
print(cal_untill(matrix))


def max_failing_sum_t(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[-1]*m for _ in range(n)]

    for j in range(m):
        dp[0][j] = matrix[0][j]

    for i in range(1,n):
        for j in range(m):
            up = dp[i-1][j]
            left = dp[i-1][j-1] if j > 0 else float('-inf')
            right = dp[i-1][j+1] if j < m - 1 else float('-inf')
            dp[i][j] = max(up,left,right) + matrix[i][j]
    
    maxi = float('-inf')
    for j in range(m):
        maxi = max(maxi,dp[n-1][j])
    return maxi
print(max_failing_sum_t(matrix))