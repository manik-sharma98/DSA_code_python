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

print(subsequences_string())

def restoreIpAddresses(s):
    ips = []
    ''''''
    def back_track(start,octets=[]):
        if len(octets) == 4 and start == len(s):
            ips.append('.'.join(octets))
            return
        for size in range(1,4):
            octet = s[start:start+size]
            if len(octet) > 1 and (octet[0]== '0' or int(octet)>255):
                continue
            if len(octets) < 4:
                octets.append(octet)
                back_track(start + size)
                octets.pop()
        
    back_track(0)
    return ips
s = '25525511135'
    
print(restoreIpAddresses(s))

