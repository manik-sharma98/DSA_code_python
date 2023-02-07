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
    
v = 4
adj = [[]for i in range(v)]
add_edge(adj,0,1)
add_edge(adj,0,2)
add_edge(adj,1,2)
add_edge(adj,1,3)
print_graph(adj)
bfs(adj,0)
dfs(adj,0)