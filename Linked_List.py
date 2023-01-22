class Node:
    def __init__(self,val,next) -> None:
        self.val = val
        self.next = None

def Linked_list():
    Head = None

def reverse(node):
    if node == None:
        return Node
    
    if node.next == None:
        return node 

    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1
    