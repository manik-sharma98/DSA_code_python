# G = (V,E)
# Two ways to represent graph
# Adjacency matrix and Adjacency List


def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def print_graph(adj):
    for l in adj:
        print(l)

def bfs(adj,s):
    visited = [False] * len(adj)
    q = []
    q.append(s)
    visited[s] = True
    while q:
        edge = q.pop(0)
        print(edge,end=' ')
        for next_edge in adj[edge]:
            if visited[next_edge] == False:
                q.append(next_edge)
                visited[next_edge] = True
    print()

def dfs(adj,s):
    visited = [False] * len(adj)
    stack = []
    stack.append(s)
    visited[s] = True
    while stack:
        s = stack.pop()
        print(s,end=' ')
        for u in adj[s]:
            if visited[u] == False:
                stack.append(u)
                visited[u] = True
    print()

def bfs_until(adj,i,visited):
    q = []
    visited[i] = True
    q.append(i)
    while q:
        v = q.pop(0)
        print(v,end=' ')
        for u in adj[v]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True

def bfs_disconnted(adj):
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if visited[i] == False:
            bfs_until(adj,i,visited)

def dfs_until(adj,i,visited):
    q = []
    visited[i] = True
    q.append(i)
    while q:
        v = q.pop()
        print(v,end=' ')
        for u in adj[v]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True

def dfs_disconnted(adj):
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if visited[i] == False:
            dfs_until(adj,i,visited)


v = 4
adj = [[]for i in range(v)]

add_edge(adj,0,1)
add_edge(adj,0,2)
add_edge(adj,1,2)
add_edge(adj,1,3)
print('Adjacency list repersentation of graph')
print_graph(adj)
print()

print('BFS for connected graph ->')
bfs(adj,0)
print()
print('DFS for connected graph ->')
dfs(adj,0)
print()

adj_disconnected = [[1, 2], [0, 3], [0, 3], [1, 2], [5, 6], [4, 6], [4, 5]]
print('BFS for disconnected graph ->')
bfs_disconnted(adj_disconnected)
print()
print('DFS for disconnected graph ->')
dfs_disconnted(adj_disconnected)
print()
