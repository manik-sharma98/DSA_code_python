mat = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dp = [[1e9]*len(mat[0]) for _ in range(len(mat))]
def getval(grid,i,j):
    n = len(grid)
    m = len(grid[0])
    if i == n or j == m:
        return 1e9
    if i == n-1 and j == m-1:
        return 1 - grid[i][j] if grid[i][j] <= 0 else 1
    if dp[i][j] != 1e9:
        return dp[i][j]
    right = getval(grid,i+1,j)
    down = getval(grid,i,j+1)
    min_req = min(right,down) - mat[i][j]
    dp[i][j] = min_req
    if min_req <= 0:
        dp[i][j] = 1
    return dp[i][j]
print(getval(mat,0,0))

def get_val_t(grid):
    
    n = len(grid)
    m = len(grid[0])
    dp = [[float('inf')]*(m+1) for _ in range(n+1)]
    dp[n][m-1] = 1
    dp[n-1][m] = 1
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            need =  min(dp[i+1][j], dp[i][j+1]) - grid[i][j]
            dp[i][j] = 1 if need <= 0 else need
    return dp[0][0]

print(get_val_t(mat))
