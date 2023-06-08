def subset_sum(i,nums,k,dp):
    if k == 0:
        return 1
    if i == 0:
        return arr[0] == k
    pick = subset_sum(i-1,nums,k-nums[i],dp)
    not_pick = subset_sum(i-1,nums,k,dp)
    return pick or not_pick
arr = [1,2,3,4]
k = 12
print(subset_sum(len(arr)-1,arr,k,0))

