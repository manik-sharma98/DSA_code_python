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
#print(insert_sort([10, 5, 8, 20, 2, 18]))

#merge_sort() -> O(n*log(n))
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
#print(merge_sort(arr,0,len(arr)-1))

#union_sorted_arrays
def unio_sorted(l1,l2):    
    i = 0
    j = 0
    k = 0
    while i < len(l1) and j < len(l2):
        if i > 0 and l1[i] == l1[i-1]:
            i += 1
        elif j > 0 and l2[j] == l2[j-1]:
            j += 1
        elif l1[i] < l2[j]:
            print(l1[i],end=' ')
            i += 1 
            k += 1
        elif l1[i] > l2[j]:
            print(l2[j],end=' ')
            j += 1 
            k += 1
        else:
            print(l1[i],end=' ')
            i += 1
            j += 1
            k += 1
    while i < len(l1):
        if i > 0 and l1[i] != l1[i-1]:
            print(l1[i],end=' ')
            i += 1
    while j < len(l2):
        if j > 0 and l2[j] != l2[j-1]:
            print(l2[j],end=' ')
            j += 1
    print(end='\n')

#unio_sorted([2,10,20,20],[2,3,20,40])

def intersection_sorted(l1,l2):
    i = 0
    j = 0 
    while i < len(l1) and j < len(l2):
        if i > 0 and l1[i] == l1[i-1]:
            i += 1
            continue
        elif l1[i] < l2[j]:
            i += 1 
        elif l1[i] > l2[j]:
            j += 1
        else:
            print(l1[i],end=' ')
            i += 1
            j += 1
    print(end='\n')
    
#intersection_sorted([2,10,20,20],[2,3,20,40])

#Quick_sort -> O(n*log(n))
def partion(nums,l,h):
    pivot = nums[h]
    i = l - 1
    for j in range(l,h):
        if nums[j] <= pivot:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[h] = nums[h],nums[i+1]
    return i + 1
def quicksort(arr,low,high):
    if low < high:
        pi = partion(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

arr = [10, 7, 8, 9, 1, 5]
quicksort(arr,0,5)
#print(arr)

#Heap Sort 
def max_heapify(nums,n,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i],nums[largest] = nums[largest],nums[i]
        max_heapify(nums,n,largest)

def bulid_heap(nums):
    n = len(nums)
    for i in range((n-2)//2,-1,-1):
        max_heapify(arr,n,i)

def heap_sort(nums):
    n = len(nums)
    bulid_heap(nums)
    for i in range(n-1,0,-1):
        nums[i],nums[0] = nums[0],nums[i]
        max_heapify(nums,i,0)

arr = [10, 7, 8, 9, 1, 5]
heap_sort(arr)
print(arr)
