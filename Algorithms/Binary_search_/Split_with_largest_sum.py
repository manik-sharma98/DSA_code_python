nums = [7,2,5,10,8]
k = 2
def cansplit(max_sum):
    sub_array = 1
    cur_sum = 0
    for n in nums:
        cur_sum += n
        if cur_sum > max_sum:
            sub_array += 1
            cur_sum = n
    return sub_array <= k
l = max(nums)
r = sum(nums)
res = r
while l <= r:
    mid = l + (r-l)//2
    if cansplit(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)