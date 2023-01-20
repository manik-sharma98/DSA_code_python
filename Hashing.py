#chaining
class MyHash():
    def __init__(self,b) -> None:
        self.Bucket = b
        self.Table = [[] for i in range(b)]
    
    def insert(self,x):
        i = x % self.Bucket
        self.Table[i].append(x)

    def remove(self,x):
        i = x % self.Bucket
        if x in self.Table[i]:
            self.Table[i].remove(x)
    
    def search(self,x):
        i = x % self.Bucket
        return x in self.Table[i]
h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.search(56))
h.remove(56)

def count_disctnt(nums):
    hash_map = {}
    for n in nums:
        if n in hash_map:
            hash_map[n] += 1
        else:
            hash_map[n] = 1
    res = 1
    for i in range(1,len(nums)):
        if nums[i] not in nums[0:i]:
            res += 1
    #return res
    return len(hash_map.keys())

print(count_disctnt([1,2,3,3,4,5,6,7,8,9,1]))