n = 3
m = 7
dp = [[-1]*(m+1) for _ in range(n+1)]
def unqiue_paths(i,j):
    if i == 0 and j ==0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    right = unqiue_paths(i-1,j)
    down = unqiue_paths(i,j-1)
    dp[i][j] = right + down
    return dp[i][j]

print(unqiue_paths(n-1,m-1))

def up_t(n,m):
    dp = [[1]*(m+1) for _ in range(n+1)]
    
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]

print(up_t(3,7))

def unqiue_paths_ob(i,j,path,dp):
    if i > 0 and j > 0 and path[i][j] ==-1:
        return 0
    if i == 0 and j ==0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    right = unqiue_paths_ob(i-1,j,path,dp)
    down = unqiue_paths_ob(i,j-1,path,dp)
    dp[i][j] = right + down
    return dp[i][j]

maze = [[0,0,0], [0,-1,0], [0,0,0]]
n = len(maze)
m = len(maze[0])
dp = [[-1]*(m+1) for _ in range(n+1)]
print(unqiue_paths_ob(n-1,m-1,maze,dp))