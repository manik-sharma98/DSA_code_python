import math
def smallestDivisor(nums: list[int], threshold: int) -> int:
    def condition(mid):
        summ = 0
        for num in nums:
            summ += math.ceil((1.0*num)/mid)
        return summ

    ans = -1
    l = 1
    r = max(nums)
    while l<= r:
        mid = (l+r)//2
        result = condition(mid)
        if result <= threshold:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

#print(smallestDivisor([44,22,33,11,1],5))


def binary_search(nums,x):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r)//2
        if nums[mid] == x:
            return mid + 1
        elif nums[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return 0
def binary_search_rec(nums,x,l,r):
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == x:
            return mid + 1
        elif nums[mid] < x:
            return binary_search_rec(nums,x,mid+1,r)
        else:
            return binary_search_rec(nums,x,l,mid-1)
    return 0
#print(binary_search_rec([1,2,4,5,6,7,8,10],10,0,8))

def bs_last_index(nums,x):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l+r)//2
        if nums[mid]<x:
            l = mid+1
        elif nums[mid]>x:
            r = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid] != nums[mid+1]:
                return mid 
            else:
                l = mid + 1
    return -1
def bs_first_index(nums,x):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r)//2
        if nums[mid] < x:
            l = mid + 1 
        elif nums[mid] > x:
            r = mid - 1
        else:
            if mid == 0 or nums[mid-1]!=nums[mid]:
                return mid
            else:
                r = mid - 1
def count_occ(nums,x):
    frist = bs_first_index(nums,x)
    if frist == -1:
        return 0
    else:
        return (len(nums) - frist)                    
#print(count_occ([0,0,1,1,1,1,1],1))

def sqrt(x):
    l = 0
    r = x
    ans = -1
    while l<=r:
        mid = (l+r) // 2
        msq = mid*mid
        if msq == x:
            return mid
        elif msq > x:
            r = mid - 1
        else:
            l = mid + 1
            ans = mid
    return ans
#print(sqrt(16))