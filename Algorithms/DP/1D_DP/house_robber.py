def house_robber(nums):
    rob1 = 0
    rob2 = 0
    for num in nums:
        newrob = max(rob1+num,rob2)
        rob1 = rob2
        rob2 = newrob
    return rob2
def rob(arr):
    return max(arr[0],house_robber(arr[1:]),house_robber(arr[:-1]))
arr = [1, 5, 1, 2, 6]
n = len(arr)
print(rob(arr))
print(house_robber(arr[1:]),arr[1:])
print(house_robber(arr[:-1]),arr[:-1])
