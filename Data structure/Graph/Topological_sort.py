from collections import defaultdict
class TP_sort():
    def __init__(self,v) -> None:
        self.graph = defaultdict(list)
        self.V = v
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topological_sort(self):
        in_degree = [0] * self.V

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
        q = []
        for i in range(self.V):
            if in_degree[i] == 0:
                q.append(i)
        res = []
        count = 0
        while q:
            v = q.pop(0)
            res.append(v)
            count += 1
            for u in self.graph[v]:
                in_degree[u] -= 1
                if in_degree[u] == 0:
                    q.append(u)
            
        if count != self.V:
            print('Cycle Found')
        else:
            return res
    
    def dfs_untill(self,v,visited,stack):
        visited[v] = True
        for u in self.graph[v]:
            if visited[u] == False:
                self.dfs_untill(u,visited,stack)
        stack.append(v)
    def dfs_topo_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
               self.dfs_untill(i,visited,stack)
        return(stack[::-1])

g = TP_sort(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print ("Following is a Topological Sort of the given graph")
print(g.topological_sort())
print ("Following is a Topological Sort of the given graph - DFS")
print(g.dfs_topo_sort())
