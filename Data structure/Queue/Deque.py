from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.pop()
d.popleft()
d.extend([4,5])
d.extendleft([1,1])
print(d)

class Mydeque():
    def __init__(self,c) -> None:
        self.l = [None] * c
        self.cap = c
        self.front = 0
        self.size = 0
    
    def insert_front(self,x):
        if self.size == self.cap:
            return
        self.front = (self.front - 1)%self.cap
        self.l[self.front] = x
        self.size += 1
        
    def insert_rear(self,x):
        if self.size == self.cap:
            return
        new_rear = (self.front + self.size)%self.cap
        self.l[new_rear] = x
        self.size += 1
    
    def delete_front(self):
        if self.size == 0:
            return
        self.front = (self.front + 1)%self.cap
        self.size -= 1
    
    def delete_rear(self):
        if self.size == 0:
            return
        rear = (self.front + self.size - 1)%self.cap
        self.size -= 1
    
    def frontEle(self):
        return self.l[self.front]

    def rearEle(self):
        rear = (self.front + self.size - 1) % self.cap
        return self.l[rear]

dq = Mydeque(4)

dq.insert_rear(10)
print(dq.frontEle(), dq.rearEle())
dq.insert_front(20)
print(dq.frontEle(), dq.rearEle())
dq.insert_front(30)
print(dq.frontEle(), dq.rearEle())
dq.delete_rear()
print(dq.frontEle(), dq.rearEle())
dq.insert_rear(40)
print(dq.frontEle(), dq.rearEle())
dq.delete_rear()
print(dq.frontEle(), dq.rearEle())


class Node():
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class my_deque_ll():
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def insert_rear(self,x):
        new_node = Node(x)
        if self.rear == None:
            self.front = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
        self.rear = new_node
        self.size += 1
    
    def delete_front(self):
        if self.front == 0:
            return
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        else:
            self.front.prev = None
        self.size -= 1
    
    def isempty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    
    def get_front(self):
        if self.front:
            return self.front.val
    
    def get_rear(self):
        if self.rear:
            return self.rear.val

dq = my_deque_ll()
print(dq.isempty())
dq.insert_rear(10)
print(dq.get_front(),dq.get_rear())
dq.insert_rear(20)
print(dq.get_front(),dq.get_rear())
dq.insert_rear(30)
print(dq.get_front(), dq.get_rear())
dq.delete_front()
print(dq.get_front(), dq.get_rear())
