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

    def print_list(self):
        temp = self.head
        while temp :
            print(temp.val,end='  ')
            temp = temp.next
    def search(self,x):
        pos = 1
        temp = self.head
        while temp:
            if temp.val == x:
                return pos
            pos += 1
            temp = temp.next
        return -1


l1 = LinkedList()
l1.push(3)
l1.push(2)
l1.push(1)
l1.append(4)
l1.insert_after(l1.head,1.5)
l1.print_list()

print('\nElement is at ',l1.search(3))

def reverse(node):
    if node == None:
        return Node
    
    if node.next == None:
        return node 

    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1
    