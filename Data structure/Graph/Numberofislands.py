def dfs_island(grid,i,j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    dfs_island(grid,i-1,j)
    dfs_island(grid,i+1,j)
    dfs_island(grid,i,j-1)
    dfs_island(grid,i,j+1)

def numberofislands(grid):
    if grid is None or len(grid) == 0:
        return 0
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs_island(grid,r,c)
                count += 1
    return count 

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
    ]
print(numberofislands(grid))