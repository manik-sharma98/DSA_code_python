import math
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.pop()
stack.pop()
print(stack)

class Node():
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
    
class stack_ll():
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def push(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def seek(self):
        if self.head is None:
            return math.inf
        return self.head.val

    def pop(self):
        self.head = self.head.next
        self.size -= 1
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.val,end = ' ')
            temp = temp.next
        print()

stck = stack_ll()
stck.push(5)
stck.push(4)
stck.push(3)
stck.push(2)
stck.push(1)
stck.pop()
stck.pop()
stck.print()
print(stck.size)

s = '()'

def is_match(a,b):
    if a == '}' and b != '{':
        return False
    if a == ')' and b != '(':
        return False
    if b == ']' and b != '[':
        return False

def check_balanced_parenthesis(s):
    stack = []
    for char in s:
        if char == '[' or char == '(' or char == '{':
            stack.append(char)
        else:
            opening_bracket = stack.pop()
            if is_match(char,opening_bracket) == False:
                return False 
    if stack:
        return False
    else:
        return True

print(check_balanced_parenthesis(s))
