def count_sub_arrays(nums):
    prefix_sum = 0
    prefix_sum_count = {0:1}
    count = 0

    for num in nums:
        if num == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1
        if prefix_sum in prefix_sum_count:
            count += prefix_sum_count[prefix_sum]
            
        print(count,prefix_sum)
        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum,0) + 1
    print(prefix_sum_count)
    return count 
arr = [ 1, 0, 0, 1, 1, 0, 0, 1]
print(count_sub_arrays(arr))