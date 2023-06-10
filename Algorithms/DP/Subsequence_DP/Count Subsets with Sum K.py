def count_subset_sum(i,k,nums,dp):
    if i == 0:
        if k == 0 and arr[0] == 0:
            return 2
        if k == 0 or k == arr[0]:
            return 1
        return 0
    if dp[i][k] != -1:
        return dp[i][k]
    not_taken = count_subset_sum(i-1,k,nums,dp)
    taken = 0
    if nums[i] <= k:
        taken = count_subset_sum(i-1,k-nums[i],nums,dp)
    dp[i][k] = not_taken + taken
    return dp[i][k]

arr = [1, 2, 2, 3]
k = 3
n = len(arr)
dp = [[-1]*(k+1) for i in range(n)]
print(count_subset_sum(n-1,k,arr,dp))

def count_subset_sum_t(k,nums):
    n = len(nums) 
    dp = [[0]*(k+1) for i in range(n)]
    for i in range(n):
        dp[i][0] = 1
    if nums[0] <= k:
        dp[0][nums[0]] = 1
    
    for i in range(1,n):
        for j in range(1,k+1):
            not_taken = dp[i-1][j]
            taken = 0
            if nums[i] <= k:
                taken = dp[i-1][j-nums[i]]
            dp[i][j] = taken + not_taken
    return dp[n-1][k]

arr = [1, 2, 2, 3]
k = 3
print(count_subset_sum_t(k,arr))
