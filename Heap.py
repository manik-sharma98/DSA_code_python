# -> used in heapsort
# -> used in priority queue
# -> max heap and min heap
# -> compelte binary tree
import math
import heapq
l1 = [1,3,4,5,2,8,7,0,9,6]
print('------heapq----------')
heapq.heapify(l1)
print(l1)
heapq.heappush(l1,10)
print(l1)
print(heapq.heappop(l1))
print(l1)
print(heapq.nlargest(2,l1))
print(heapq.nsmallest(2,l1))
print(heapq.heappushpop(l1,11))
print(heapq.nlargest(1,l1))
print('--------------------')

class minHeap():
    def __init__(self) -> None:
        self.arr = []
    
    def parent(self,i):
        return (i-1) // 2
    
    def lchild(self,i):
        return 2*i+1
    
    def rchild(self,i):
        return 2*i+2

    def insert(self,x):
        arr = self.arr
        arr.append(x)
        i = len(arr) - 1
        
        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i],arr[p] = arr[p],arr[i]
            i = p
 
    def minHeapify(self,i):
        arr = self.arr
        lt = self.lchild(i)
        rt = self.rchild(i)
        smallest = i
        n = len(arr) - 1
        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt
        if smallest != i:
            arr[i],arr[smallest] = arr[smallest],arr[i]
            self.minHeapify(smallest)
        

    def extractmin(self):
        arr = self.arr
        arr[0],arr[-1] = arr[-1],arr[0]
        min_no = arr.pop()
        self.minHeapify(0)
        return min_no

    def decrease(self,i,x):
        arr = self.arr
        arr[i] = x
        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[p],arr[i] = arr[i],arr[p]
            i = p
    
    def delete(self,i):
        self.decrease(i,-math.inf)
        self.extractmin()

heap = minHeap()
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.delete(6)
print(heap.extractmin())
print(heap.arr)
