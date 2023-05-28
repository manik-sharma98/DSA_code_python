def b_s(a,target):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l+r)//2
        if mid == target:
            return mid
        elif mid < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

a = [1,2,3,4,5,6,7,8,9]
print(b_s(a,7))