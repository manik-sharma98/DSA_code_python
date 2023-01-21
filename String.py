print(ord('a'))
print(chr(97))
print(ord('A'))
name = 'Manik'
Age = 24
print('My Name is {0} and age is {1}'.format(name,Age))
print(f'My Name is {name} and age is {Age}')
s1 = 'GeeksforGeeks'
s2 = 'Geeks'
print(s2 in s1)
print(s2 not in s1)
print(s1.index(s2))
s = 'geeks'
s3 = ''
for c in s:
    s3 += ''.join(chr(ord(c)-32))
print(s3)

def is_subq(a,b):
    if a == b:
        return True
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(b):
        return True
    else:
        return False
print(is_subq('abcde','aed')) 

def are_anagram(a,b):
    if len(a) != len(b):
        return False
    count = [0]*256
    for i in range(len(a)):
        count[ord(a[i])] += 1
        count[ord(b[i])] -= 1
    for x in count:
        if x != 0:
            return False
    return True
print(are_anagram('aabca','abcaa'))

def lmo(s):
    if s == set(s):
        return -1
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return i
    return -1
print(lmo('abccd'))

def lmo_o(s):
    visited = [False]*256
    res = -1
    for i  in range(len(s)-1,-1,-1):
        if visited[ord(s[i])] == True:
            res = i
        else:
            visited[ord(s[i])] = True
    return res
print(lmo_o('abccd'))

def non_rep(s):
    count = [0]*256
    for c in s:
        count[ord(c)] += 1
    for i in range(len(s)):
        if  count[ord(s[i])] == 1:
            return i
    return -1 
print(non_rep('abccd'))
