def subset_sum(i,k,nums,dp):
    if i == 0:
        if k == 0 and nums[0] == 0:
            return 2
        if k == 0 or k == nums[0]:
            return 1
        return 0
    if dp[i][k] != -1:
        return dp[i][k]
    not_taken = subset_sum(i-1,k,nums,dp)
    taken = 0
    if nums[0] <= k:
        taken = subset_sum(i-1,k-nums[i],nums,dp)
    dp[i][k] = not_taken + taken
    return dp[i][k]

def count_part(nums,d):
    n = len(nums)
    total_sum = sum(nums)

    if total_sum - d < 0:
        return 0
    if (total_sum-d) % 2 != 0:
        return 0
    s2 = (total_sum-d) // 2

    dp = [[-1]*(s2+1) for i in range(n+1)]
    return subset_sum(n-1,s2,nums,dp)
arr = [5, 2, 6, 4]
d = 3
print(count_part(arr,d))

def find_ways(nums,k):
    n = len(nums)
    dp = [[0]*(k+1) for i in range(n)]

    if nums[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1

    if nums[0] != 0 and nums[0] <= k:
        dp[0][nums[0]] = 1
    
    for i in range(1,n):
        for j in range(k+1):
            not_pick = dp[i-1][j]
            pick = 0
            if nums[i] <= k:
                pick = dp[i-1][j-nums[i]]

            dp[i][j] = (not_pick+pick) % (1e9+7)
    return dp[n-1][k]
total_sum = sum(arr)
print(find_ways(arr,(total_sum-d)//2))
    
    
