def subsequences():
    res = []
    
    def back_track(nums,index,curr_start):
        res.append(list(curr_start))
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            curr_start.append(nums[i])
            back_track(nums,i+1,curr_start)
            curr_start.pop()
        
    curr_start = []
    nums = [4,6,7,7]
    back_track(nums,0,curr_start)
    return res

def subsequences_string():
    res = set()
    
    def back_track(nums,index,curr_start):
        res.add("".join(curr_start))
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            curr_start.append(nums[i])
            back_track(nums,i+1,curr_start)
            curr_start.pop()
        
    curr_start = []
    nums = "abc"
    back_track(nums,0,curr_start)
    return res
	
	
print(subsequences())