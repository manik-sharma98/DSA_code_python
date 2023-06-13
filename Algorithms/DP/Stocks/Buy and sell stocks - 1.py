def buy_sell(nums):
    max_profit = -1e9
    mini = nums[0]

    for i in range(1,len(nums)):
        cur_profit = nums[i] - mini
        max_profit = max(max_profit,cur_profit)
        mini = min(mini,nums[i])
    return max_profit
print(buy_sell([7,1,5,3,6,4]))