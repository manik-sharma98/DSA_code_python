def subset_sum(i,nums,k,dp):
    if k == 0:
        return 1
    if i == 0:
        return arr[0] == k
    if dp[i][k] != False:
        return dp[i][k]
    pick = subset_sum(i-1,nums,k-nums[i],dp)
    
    not_pick = subset_sum(i-1,nums,k,dp)
    dp[i][k] =pick or not_pick 
    return dp[i][k]
arr = [1,2,3,4]
k = 10
n = len(arr) 
dp = [[False]*(k+1) for _ in range(n)]
print(subset_sum(len(arr)-1,arr,k,dp))

def subset_sum_t(nums,target):
    n = len(nums)
    dp = [[False]*(k+1) for i in range(n)]
    for i in range(n):
        dp[i][0] = True
    
    if nums[0] <= target:
        dp[0][nums[0]] = True
    
    for i in range(1,n):
        for j in range(1,k+1):
            not_taken = dp[i-1][j]
            taken = 0
            if nums[i] <= target:
                taken = dp[i-1][j-nums[i]] 
            dp[i][j] = not_taken or taken
    return dp[n-1][k]

arr = [1,2,3,4]
k = 12
print(subset_sum_t(arr,k))
