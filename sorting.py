l = [1,2,3,4]
l.sort(reverse=True)
#print(l)

string_list = ['abcd','abc','abcdef','abcde']
string_list.sort(key = len)
#print(string_list)

strr = 'bcdaef'
#print(sorted(strr))

nums = [1,10,4,5,7,2,9,8,3]

#Bubble_sort
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] > nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
print(nums)
