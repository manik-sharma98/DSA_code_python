import math
from collections import deque
class Node:
    def __init__(self,val) -> None:
        self.left = None
        self.right = None
        self.val = val 

#Traversal :->
# --- Breath first (level order) (iterative)
# --- Depth first (recursive/iterative)
    # Preorder -> R,L,R
    # Inorder -> L,R,R
    # Postorder -> L,R,R

# O(n) and space - O(H)
def preorder(root):
    if root != None:
        print(root.val, end = ' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.val, end = ' ')
        inorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end = ' ')
    
def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    h = 1 + max(lh,rh)
    return h
    
def print_k_distance(root,k):
    if root == None:
        return 0
    if k == 0:
        print(root.val,end=' ')
    else:
        print_k_distance(root.left,k-1)
        print_k_distance(root.right,k-1)
    
def bfs(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.val,end = ' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
def dfs(root):
    current = root
    stack = []
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.val,end=' ')
            current = current.right
        else:
            break
def max_val(root):
    q = deque()
    q.append(root)
    max_value = -math.inf
    while q:
        node = q.popleft()
        max_value = max(node.val,max_value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return max_value
def size(root):
    q = deque()
    q.append(root)
    size = 0
    while q:
        node = q.popleft()
        size += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return size
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print('Preorder of binary tree -> ')
preorder(root)
print()
print('Inorder of binary tree -> ')
inorder(root)
print()
print('Postorder of binary tree -> ')
postorder(root)
print()
print('Height of binary tree is ->',height(root))
print()
print('Height of binary tree is ->',height(root))
print('Nodes from k distance is ->')
print_k_distance(root,2)
print()
print('BFS->')
bfs(root)
print()
print('DFS->')
dfs(root)
print()
print('Maximum value in tree is ->',max_val(root))
print('Size tree is ->',size(root))
