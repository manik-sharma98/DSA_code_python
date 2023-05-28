def b_s(a,target):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l+r)//2
        if a[mid] == target:
            if a[mid-1] != target or  mid == 0:
                return mid 
            else:
                r = mid - 1
        elif mid < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def b_s_last(a,target):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l+r)//2
        if a[mid] == target:
            if a[mid+1] != target or  mid == len(a)-1:
                return mid
            else:
                l = mid + 1
        elif mid < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


a = [1,2,2,2,2,4,5,6,7,8,9]
print(b_s(a,2))
print(b_s_last(a,2))

s = 'abcabcbb'

s1 = 'pwwkew'

def long_sub_string(s):
    l = 0
    r = 1
    ans = ''
    out = ''
    max_len = 0
    while l <= r and r <= len(s) - 1:
        ans = s[l:r+1]
        if s[r] not in ans:
            r += 1
        else:
            l += 1
        leng = r - l + 1
        if max_len <= leng:
            max_len = leng
            out = ans
    print(out)
long_sub_string(s1)

def fac(n):
    if n == 1 :
        return 1
    return n * fac(n-1)
print(fac(5))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(6))

def rec(arr,i):
    if i == 0:
        return arr[0] 
    print(arr[i],end=' ')
    return rec(arr,i-1)

a = [1,2,2,2,2,4,5,6,7,8,9]
print(rec(a,len(a)-1))

def palin(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
print(palin('racecar'))
