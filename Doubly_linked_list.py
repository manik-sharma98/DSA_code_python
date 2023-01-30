class Node():
    def __init__(self,val) -> None:
        self.val = val
        self.prev = None
        self.next = None

class dll():
    def __init__(self) -> None:
        self.head = None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        new_node.prev = None
        if self.head != None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self,prev_node,val):
        new_node = Node(val)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next != None:
            new_node.next.prev = new_node
        
    def insert_end(self,val):
        new_node = Node(val)
        last = self.head
        while last.next:
            last = last.next
        new_node.next = None
        last.next = new_node
        new_node.prev = last
    
    def pop(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    def delete(self,val):
        temp = self.head
        prev_node = None
        while temp:
            if temp.next == None:
                self.pop()
                return
            if temp.val == val:
                break
            prev_node = temp
            temp = temp.next
        prev_node.next = temp.next
        temp.next.prev = prev_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.val,end=' ')
            temp = temp.next
        
    def reverse(self):
        temp = self.head
        prev_node = None
        while temp:
            prev_node = temp
            temp.next,temp.prev = temp.prev,temp.next
            temp = temp.prev
        while prev_node:
            print(prev_node.val,end=' ')
            prev_node = prev_node.next
        
d1 = dll()
d1.push(3)
d1.push(2)
d1.push(1)
d1.insert_end(4)
d1.insert_end(5)
d1.pop()
d1.delete(4)
d1.print()
d1.reverse()
