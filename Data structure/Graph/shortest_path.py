from collections import defaultdict
import math
import heapq
class shortest_path():
    def __init__(self,v) -> None:
        self.graph = defaultdict(list)
        self.V = v
    
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))
    
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
    
    def dijkstra(self,k):
        heap = [(0,k)]
        dist = [0] + [float('inf')] * (self.V-1)
        while heap:
            weight,next_city = heapq.heappop(heap)
            for j,w in self.graph[next_city]:
                if dist[j] > dist[next_city] + w:
                    dist[j] = dist[next_city] + w
                    heapq.heappush(heap,(dist[j],j))
        return dist
        

g = shortest_path(9)
'''
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
'''
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)
print(g.dijkstra(0))