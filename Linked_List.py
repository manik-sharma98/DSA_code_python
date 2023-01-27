class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self,data):
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = Node(data)
        temp.next = new_node

    def insert_after(self,prev_node,data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def del_frist(self):
        if self.head == None:
            return None
        else:
            self.head = self.head.next

    def delete(self,val):
        temp = self.head
        prev = None
        while temp:
            if temp.val == val:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def pop(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def sorted_insert(self,data):
        temp = self.head
        while temp:
            if temp.val > data:
                break
            prev = temp
            temp = temp.next
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node
            
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val,end='  ')
            temp = temp.next
     
    
    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print('Middle of linked list -->',slow.val)
    
    def search(self,x):
        pos = 1
        temp = self.head
        while temp:
            if temp.val == x:
                return pos
            pos += 1
            temp = temp.next
        return -1

    def nthfromlast(self,n):
        frist = self.head
        second = self.head
        for i in range(n):
            frist = frist.next
        while frist:
            frist = frist.next
            second = second.next
        print('Nth node from last -->',second.val)

l1 = LinkedList()
l1.push(30)
l1.push(20)
l1.push(10)
l1.append(40)
l1.insert_after(l1.head,15)
#l1.pop()
l1.delete(20)
l1.sorted_insert(20)
l1.sorted_insert(25)
l1.print_list()
print('\n')
l1.middle()
l1.nthfromlast(2)
l1.del_frist()
print('Element is at',l1.search(30),'Postion')

def reverse(node):
    if node == None:
        return Node
    
    if node.next == None:
        return node 

    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1
    