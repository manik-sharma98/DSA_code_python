#FIFO
q = []
q.append(10)
q.append(20)
q.append(30)

print(q)
print(q.pop(0))
print(q)
q.append(40)
print(q)
print(q.pop(0))
print(q)
print(len(q))
print(q[0])
print(q[-1])


class queue():
    def __init__(self,c) -> None:
        self.q = [] 
        self.size = 0
        self.cap = c
    def enqueue(self,x):
        if self.cap == self.size:
            print('Queue is Full')
        else:
            self.q.append(x)
            self.size += 1
        
    def dequeue(self):
        if self.size == 0:
            print('Queue is empty')
        else:
            self.q.pop()
            self.size -= 1

    def getFront(self):
        return self.q[0]

    def getrear(self):    
        return self.q[-1]

    def isEmpty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
q = queue(5)
q.dequeue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
print(q.q)
q.dequeue()
q.dequeue()
print(q.q)

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
    
class queue_ll():
    def __init__(self) -> None:
        self.size = 0
        self.front = None
        self.rear = None

    def enqueue(self,x):
        new_node = Node(x)
        if self.rear == None:
            self.front = new_node
        else:
            self.rear.next = new_node
        
        self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if self.front == None:
            return
        else:
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.size -= 1
    
    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def getFront(self):
        return self.front.val

    def getRear(self):
        return self.rear.val

q = queue_ll()
q.enqueue(10)
print(q.getFront(), q.getRear())
q.enqueue(20)
print(q.getFront(), q.getRear())
q.enqueue(30)
print(q.getFront(), q.getRear())
q.dequeue()
print(q.getFront(), q.getRear())