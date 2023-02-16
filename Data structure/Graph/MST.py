import heapq
from collections import defaultdict
class prims():
    def __init__(self,v) -> None:
         self.graph = defaultdict(list)
         self.V = v
        
    def add_edge(self,u,v,w):
        
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))

    def prims_imp(self):    
        visited = set()
        cost = 0
        heap = [(0,1)]
        while heap:
            min_cost,city = heapq.heappop(heap)
            if city not in visited:
                cost += min_cost
                visited.add(city)
                for next,next_w in self.graph[city]:
                    if next not in visited:
                        heapq.heappush(heap,(next_w,next))
        return -1 if len(visited) < self.V else cost

g = prims(3)
connections = [[1,2,5],[1,3,6],[2,3,1]]
for r in range(len(connections)):
    g.add_edge(connections[r][0],connections[r][1],connections[r][2])
    print(connections[r][0],connections[r][1],connections[r][2])
print(g.prims_imp())