# -> used in heapsort
# -> used in priority queue
# -> max heap and min heap
# -> compelte binary tree

class minHeap():
    def __init__(self) -> None:
        self.arr = []
    
    def parent(self,i):
        return (i-1) // 2
    
    def lchild(self,i):
        return 2*i+1
    
    def rchild(self,i):
        return 2*i+1

    def insert(self,x):
        arr = self.arr
        arr.append(x)
        i = len(arr) - 1
        
        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i],arr[p] = arr[p],arr[i]
            i = p
 
    def minHeapify(self,i):
        pass

    def extractmin(self,i):
        pass

    def decrease(self,i):
        pass
    
    def delete(self,i):
        pass