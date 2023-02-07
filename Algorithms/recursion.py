#interation
def fib(n):
    a = 0
    b = 1
    print(a,b)
    for i in range(2,n):
        c = a+b
        print(c,end=' ')
        a = b
        b = c
#Rercusion
def fib_r(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_r(n-1) + fib_r(n-2)
fib(10)
print(fib_r(10))

def rec(n):
    if n == 0:
        return n
    print(n,end=' ')
    rec(n-1)
    

def sum(n):
    if n == 0:
        return 0
    return n%10 + sum(n//10)
