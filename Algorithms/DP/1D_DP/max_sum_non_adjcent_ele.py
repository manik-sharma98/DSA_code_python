def max_sum(i,nums):
    if i == 0:
        return nums[i]
    if i < 0:
        return 0
    pick = nums[i] + max_sum(i-2,nums)
    not_pick = 0 + max_sum(i-1,nums)
    return max(pick,not_pick) 
arr = [2, 1, 4, 9]
n = len(arr)
print(max_sum(n-1, arr))

dp = [-1] * n
def max_sum_m(i,nums):
    if i == 0:
        return dp[0]
    if i < 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    pick = nums[i] + max_sum(i-2,nums)
    not_pick = 0 + max_sum(i-1,nums)
    dp[i] = max(pick,not_pick) 
    return  dp[i]
arr = [2, 1, 4, 9]
n = len(arr)
print(max_sum_m(n-1, arr))

def max_sum_m(n,nums):
    dp = [-1] * len(nums) 
    dp[0] = nums[0]
    for i in range(1,len(nums)):
        pick = nums[i]
        if i > 1:
            pick +=  dp[i-2]
        not_pick = 0 + dp[i-1]
        dp[i] = max(pick,not_pick) 
    
    return  dp[n]
arr = [2, 1, 4, 9]
n = len(arr)
print(max_sum_m(n-1, arr))