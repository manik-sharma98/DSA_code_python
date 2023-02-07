import math
def addEdge(adj,u,v):
    adj[v].append(u)
    adj[u].append(v)

def shortest_bfs(adj,s):
    q = []
    q.append(s)
    visited = [False] * len(adj)
    visited[s] = True
    dist = [math.inf] * len(adj)
    dist[0] = 0
    while q:
        v = q.pop(0)
        for u in adj[v]:
            if visited[u] == False:
                dist[u] = dist[v] + 1
                print(dist[u])
                q.append(u)
                visited[u] = True
    return dist

def dfs_cycle(adj,i,visited,parent):
    visited[i] = True
    for v in adj[i]:
        if visited[v] == False:
            dfs_cycle(adj,v,visited,i)
        elif v != parent:
            return True
    return False

def DFS(adj,s):
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if visited[i] == False:
            if dfs_cycle(adj,i,visited,-1):
                return True
    return False

def dfs_cycle_connected(adj,i,visited,rec_stack):
    visited[i] = True
    rec_stack[i] = True

    for v in adj[i]:
        if visited[i] == False:
            if dfs_cycle_connected(adj,v,visited,rec_stack):
                return True
        elif rec_stack[v] == True:
            return True
    
    rec_stack[i] = True
    return False

def DFS_directed(adj,s):
    visited = [False]  * len(adj)
    rec_stack = [False] * len(adj)
    for i in range(len(adj)):
        if visited[i] == False:
            if dfs_cycle_connected(adj,i,visited,rec_stack):
                return True
    return False

v = 4 
adj = [[] for i in range(v)]

addEdge(adj,0,1)
addEdge(adj,1,2)
addEdge(adj,2,3)
addEdge(adj,0,2)
addEdge(adj,0,3)
print(shortest_bfs(adj,0))

adj_cycle = [[] for i in range(v)]

addEdge(adj_cycle,0,1)
addEdge(adj_cycle,1,2)
addEdge(adj_cycle,2,3)
addEdge(adj_cycle,0,2)
addEdge(adj_cycle,0,3)

no_adj_cycle = [[] for i in range(v)]
addEdge(no_adj_cycle,0,1)
addEdge(no_adj_cycle,1,2)

print(DFS(no_adj_cycle,0))
print(DFS(adj_cycle,0))
print(DFS_directed(adj_cycle,0))
