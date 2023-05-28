import math
n = [1,3,7,-6,2,0,9]
sum_arr = [0]* len(n) 

for i in range(len(n)):
    sum_arr[i] = sum_arr[i-1] + n[i]

print(sum_arr)

arr = [4,3,2,1,0]
print(arr[::-1])
print(arr[::-1]==sorted(arr))

mat = [[1,1],[1,1]]

row = len(mat)
col = len(mat[0])
final_sum = 0
for r in range(row):
    for c in range(col):
        sub_r = (r+1)*(c+1)
        sub_c = (row-r)*(col-c)
        final_sum += sub_r*sub_c*mat[r][c]

print(final_sum)

arr = [1, 2, 3, -4, -1, 4]
neg = []
pos= []
for num in arr:
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)

neg_l = 0
pos_l = 0
new_arr = []
while neg_l <= len(neg) -1 or pos_l <= len(pos) - 1 and len(pos) > 0 and len(neg) > 0 :
    new_arr.append(neg.pop(0))
    neg_l += 1
    new_arr.append(pos.pop(0))
    pos_l += 1
    

i = 0
while i <= len(pos) and len(pos) > 0:
    new_arr.append(pos.pop())
    i += 1
j = 0
while j <= len(neg) and len(neg) > 0:
    new_arr.append(neg.pop())
    j += 1

print(new_arr)

n = 21
i = 1
while i*i <= n:
    if n%i==0:
        print(i)
        if n//i!=i:
            print(n//i)
    i += 1

a = [1,2,3,4,5,6,7,8,9]

l = 0
r = len(a) - 1
target = 8
while l<=r:
    mid = (l+r)//2
    if a[mid] < target:
        l = mid + 1
    elif a[mid] > target:
        r = mid -1
    else:
        print('Found at =',mid)
        break