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