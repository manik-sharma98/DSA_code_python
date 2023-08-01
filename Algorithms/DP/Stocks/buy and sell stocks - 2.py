def buy_sell(i,n,buy,dp):
    if i == len(n):
        return 0
    if dp[i][buy] != -1:
        return dp[i][buy]
    if buy == 0: # We can buy the stock  
        op1 = 0 + buy_sell(i+1,n,0,dp)
        op2 = -n[i] + buy_sell(i+1,n,1,dp)
        profit = max(op1,op2)
    if buy == 1: # We can sell the stocks
        op1 = 0 + buy_sell(i+1,n,1,dp)
        op2 = n[i] + buy_sell(i+1,n,0,dp)
        profit = max(op1,op2)
    dp[i][buy] = profit
    return dp[i][buy]

stocks = [7,1,5,3,6,4]
dp = [[-1]*(2) for i in range(len(stocks)+1)]
print(buy_sell(0,stocks,0,dp))

def buy_sell_t(nums):
    n = len(nums)
    dp = [[0] * 2 for i in range(n+1)]

    for ind in range(n-1, -1, -1):
        for buy in range(2):
            if buy == 0:
                op1 = dp[ind+1][0]
                op2 = -nums[ind]+dp[ind+1][1]
                dp[ind][buy] = max(op1,op2)
            else:
                op1 = dp[ind+1][1]
                op2 = nums[ind]+dp[ind+1][0]
                dp[ind][buy] = max(op1,op2)
    return dp[0][0]

print(buy_sell_t(stocks))

def buy_sell_simple(nums):
    profit = 0

    for i in range(1,len(nums)-1):
        if stocks[i] > stocks[i-1]:
            profit += stocks[i] - stocks[i-1]
    return profit
print(buy_sell_simple(stocks))
