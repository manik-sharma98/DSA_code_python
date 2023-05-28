import sys
def frog_jump(n,nums):
    if n == 0:
        return 0
    jump_one = frog_jump(n-1,nums) + abs(nums[n]-nums[n-1])
    jump_two = sys.maxsize
    if n > 1:
        jump_two = frog_jump(n-2,nums) + abs(nums[n]-nums[n-2])
    return min(jump_one,jump_two)

height = [30, 10, 60, 10, 60, 50]
print(frog_jump(len(height)-1,height))

dp = [-1] * len(height)
def frog_jump_m(n,nums):
    if n == 0:
        dp[n] = 0
    if dp[n] != -1:
        return dp[n]
    jump_one = frog_jump(n-1,nums) + abs(nums[n]-nums[n-1])
    jump_two = sys.maxsize
    if n > 1:
        jump_two = frog_jump(n-2,nums) + abs(nums[n]-nums[n-2])
    dp[n] = min(jump_one,jump_two)
    return dp[n]

height = [30, 10, 60, 10, 60, 50]
print(frog_jump_m(len(height)-1,height))

def frog_jump_t(n,nums):
    dp = [-1] * (len(nums)) 
    dp[0] = 0
    jump_two = sys.maxsize
    for i in range(1,n):
        jump_two = float('inf')
        jump_one = dp[i-1] + abs(nums[i]-nums[i-1])
        if i > 1:
            jump_two = dp[i-2]+ abs(nums[i]-nums[i-2])
        dp[i] = min(jump_one,jump_two)
    return dp[n-1]

print(frog_jump_t(len(height),height))

