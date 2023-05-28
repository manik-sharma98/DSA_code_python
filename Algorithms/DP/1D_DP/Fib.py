def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))

dp = [None] * 100
def fib_m(n):
    if n == 0 or n == 1:
        dp[n] = n
    if dp[n] != None:
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
print(fib_m(10))