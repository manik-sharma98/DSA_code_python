
class Node:
    def __init__(self,Data) -> None:
        self.Data = Data
        self.next = None
    
class circular_linked_list():
    def __init__(self):
        self.tail = None
        
    def push(self,data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
            self.tail.next = self.tail
            return self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
            return self.tail

    def del_end(self,tail):
        temp = self.tail
        
        while temp.next != self.tail:
            temp = temp.next
        
        temp.next = tail.next
        tail = temp.next
        print(self.tail.Data)
        print(tail.Data)
        
        return self.tail

    def delete(self,data):
        
        d = None
        cur = self.tail
        while cur.next!=self.tail and cur.next.Data!=data:
            cur = cur.next
        if cur.next.Data == data:
            d = cur.next
            cur.next = d.next
        
        return self.tail

    def print(self):
        if self.tail == None:
            return
        cur = self.tail.next
        while cur:
            print(cur.Data,end=' ')
            cur = cur.next
            if cur == self.tail.next:
                break
        print()
        
l1 = circular_linked_list()
l1.tail = l1.push(10)
l1.tail = l1.push(20)
l1.tail = l1.push(30)
l1.tail = l1.push(40)
l1.tail = l1.push(50)

l1.tail = l1.delete(20)
l1.tail = l1.delete(40)
l1.tail = l1.del_end(l1.tail)



l1.print()

