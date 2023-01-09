l = [1,2,3,4]
l.sort(reverse=True)
#print(l)

string_list = ['abcd','abc','abcdef','abcde']
string_list.sort(key = len)
#print(string_list)

strr = 'bcdaef'
#print(sorted(strr))

nums = [1,10,4,5,7,2,9,8,3]

#Bubble_sort --> O(n^2)
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] > nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
#print(nums)

#Selection_sort --> O(n^2)
def select_sort(nums):
    n = len(nums) 
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums
#print(select_sort([10, 5, 8, 20, 2, 18]))


#Insertion_sort --> O(n^2)
def insert_sort(nums):
    n = len(nums)
    for i in range(1,n):
        x = nums[i]
        j = i-1
        while j>= 0 and x>nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = x
    return nums
print(insert_sort([10, 5, 8, 20, 2, 18]))

#merge_sort()
def merge(nums,low,mid,high):
    l1 = nums[low:mid+1]
    l2 = nums[mid+1:high+1]
    i,j = 0,0
    k = low
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            nums[k] = l1[i]
            i += 1
            k += 1
        else:
            nums[k] = l2[j]
            j += 1
            k += 1
    while i < len(l1):
        nums[k] = l1[i]
        i += 1
        k += 1
    while j < len(l2):
        nums[k] = l2[j]
        j += 1
        k += 1

def merge_sort(nums,l,r):
    if r>l:
        mid = (l+r)//2
        merge_sort(nums,l,mid)
        merge_sort(nums,mid+1,r)
        merge(nums,l,mid,r)
    return nums
arr = [10, 5, 30, 15, 7]
print(merge_sort(arr,0,len(arr)-1))

