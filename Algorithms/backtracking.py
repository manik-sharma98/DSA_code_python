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

#print(subsequences_string())

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
    
#print(restoreIpAddresses(s))

def partition(s):
    res = []
    def is_palin(s):
        return s ==s[::-1]
    def back_track(s,index,cur_str):
        if index == len(s):
            res.append(list(cur_str))
            return
        for i in range(index,len(s)):
            can = s[index:i+1]
            #print(can)
            if can != can[::-1]:
                continue
            cur_str.append(can)
            back_track(s,i+1,cur_str)
            cur_str.pop()
    cur = []
    back_track(s,0,cur)
    return res
#print(partition('aab'))


def substring(s):
    all_sub_string = set()
    def back_track(s,index,sub_string):
        all_sub_string.add(''.join(sub_string))
        for i in range(index,len(s)):
            cur_string = s[index:i+1]
            sub_string.append(cur_string)
            back_track(s,i+1,sub_string)
            sub_string.pop()
    back_track(s,0,sub_string=[])
    return all_sub_string

def subseqeunce(s):
    all_sub_string = []
    def back_track(s,index,sub_string):
        all_sub_string.append(''.join(sub_string))
        for i in range(index,len(s)):
            sub_string.append(s[i])
            back_track(s,i+1,sub_string)
            sub_string.pop()
    back_track(s,0,sub_string=[])
    return all_sub_string
print(subseqeunce('abc'))
print(substring('abc'))

