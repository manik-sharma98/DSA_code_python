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

#open addressing
class myHash():
    def __init__(self,c) -> None:
         self.cap = c
         self.table = [-1]*c
         self.size = 0
    
    def Hash(self,x):
        return x % self.cap
    
    def search(self,x):
        h = self.Hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                return True
            i = (i+1)%self.cap
            if i == h:
                return False
        return False

    def insert(self,x):
        if self.size == self.cap:
            return False
        if self.search(x):
            return False
        i = self.Hash(x)
        t = self.table
        while t[i] not in (-1,-2):
            i = (i+1) % self.cap
        t[i] = x
        self.size += 1
    def remove(self,x):
        if self.size == 0:
            return False
        if self.search(x) == False:
            return False
        h = self.Hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True
            i = (i+1) % self.cap
            if i == h:
                return False
        return False
        
    
h = myHash(7)
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

#set
s1 = {10,20,30}
s2 = {20,30,40}
l1 = [1,2,3,4,5]
print(type(s1)) #check Type
print(s1|s2)    #Union
print(s1&s2)    #intersection
s1.update(l1)   #Add list to set
print(s1-s2)    #Difference
print(s1^s2)    #Not common in both
print(s1<=s2)   #subset
print(s1<s2)    #proper subset
print(s1>=s2)   #super set of s1
print(s1>s2)    #proper super set 