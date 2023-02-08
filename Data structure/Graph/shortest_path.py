from collections import defaultdict
import math
class shortest_path():
    def __init__(self,v) -> None:
        self.graph = defaultdict(list)
        self.V = v
    
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
    
    def dfs_untill(self,v,visited,stack):
        
        visited[v] = True
        if v in self.graph.keys():
            for u,w in self.graph[v]:
                if visited[u] == False:
                    self.dfs_untill(u,visited,stack)
            
        stack.append(v)
    
        
    def shortest_path_topo_sort(self,s):
        dist = [math.inf] * self.V
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.dfs_untill(i,visited,stack)
        dist[s] = 0
        
        while stack:
            i = stack.pop()

            for v,w in self.graph[i]:
                if dist[v] > dist[i] + w:
                    dist[v] = dist[i] + w
        
        for i in range(self.V):
            print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")

g = shortest_path(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
g.shortest_path_topo_sort(1)