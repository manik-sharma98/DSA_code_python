def subset_sum(i,k,nums,dp):
    if i == 0:
        return nums[0] == k
    if k == 0:
        return True
    if dp[i][k] != -1:
        return dp[i][k]
    not_taken = subset_sum(i-1,k,nums,dp)
    taken = False
    if nums[i] <= k:
        taken = subset_sum(i-1,k-nums[i],nums,dp)
    dp[i][k] = taken or not_taken
    return dp[i][k]

def get_subset_sum(nums):
    k = sum(nums)
    if k%2 != 0:
        return False
    else:
        k = k // 2
        dp = [[-1]*(k+1) for _ in range(len(nums))]
        return subset_sum(len(nums)-1,k,nums,dp)
arr = [2, 3, 3, 3, 4, 5]
print(get_subset_sum(arr))

def subset_sum_t(nums):
    k = sum(nums)
    if k%2 != 0:
        return False
    k = k //2
    n = len(nums)
    dp = [[False] * (k+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    if nums[0] <= k:
        dp[0][nums[0]] = True
    for i in range(1,n):
        for j in range(1,k+1):
            not_taken = dp[i-1][j]
            taken = False
            if nums[i] <= k:
                taken = dp[i-1][j-nums[i]]
            dp[i][j] = not_taken or taken
    return dp[n-1][k]
arr = [2, 3, 3, 3, 4, 5, 1, 1]
print(subset_sum_t(arr))