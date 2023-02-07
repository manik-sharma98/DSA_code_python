#   20
#  /  \
#10    30
from collections import deque
class Node():
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right= None

class BST():
    def search(self,root,x):
        if root is None:
            return False
        elif root.val == x:
            return True
        elif root.val < x:
            return self.search(root.right,x)
        else:
            return self.search(root.left,x)
    
    def search_it(self,root,x):
        while root != None:
            if root.val == x:
                return True
            elif root.val > x:
                root = root.left
            else:
                root = root.right
        return False
    
    def insert(self,root,x):
        if root is None:
            return Node(x)
        else:
            if root.val == x:
                return root
            elif root.val > x:
                root.left = self.insert(root.left,x)
            else:
                root.right = self.insert(root.right,x)
        return root

    def insert_it(self,root,x):
        parent = None
        curr = root

        while curr != None:
            parent = curr

            if curr.val == x:
                return root
            elif curr.val < x:
                curr = curr.left
            else:
                curr = curr.right
        if parent == None:
            return Node(x)

        if parent.val > x:
            parent.left = Node(x)
        else:
            parent.right = Node(x)

        return root

    def delete(self,root,x):
        if root is None:
            return
        elif root.val > x:
            root.left = self.delete(root.left,x)
        elif root.val < x:
            root.right = self.delete(root.right,x)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                succ = self.get_suc(root.right)
                root.val = succ
                root.right = self.get_suc(root.right,succ)
        return root

    def get_suc(self,root):
        while root:
            root = root.left
        return root.val
    
    def ceil(self,root,x):
        res = 0
        while root:
            if root.val == x:
                return root
            elif root.val > x:
                res = root.val
                root = root.left
            else:
                root = root.right
        return res
    
    def floor(self,root,x):
        res = 0
        while root:
            if root.val == x:
                return root
            elif root.val > x:
                root = root.left
            else:
                res = root.val
                root = root.right
        return res
    
    def minValue(self,root):
        if root is None:
            return -1
        cur = root
        while cur.left:
            cur = cur.left
        return cur.val
        
    def print_bfs(self,root):
        q = deque()
        q.append(root)
        while q:
            node = q.pop()
            print(node.val,end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()

bst = BST()
root = None
root = bst.insert(root,10)
root = bst.insert(root,20)
root = bst.insert(root,30)
root = bst.insert(root,40)
root = bst.insert(root,50)
root = bst.insert(root,60)
root = bst.insert(root,70)
bst.print_bfs(root)
root = bst.delete(root,60)
root = bst.delete(root,70)
bst.print_bfs(root)
print(bst.floor(root,45))
print(bst.ceil(root,35))
print(bst.minValue(root))
