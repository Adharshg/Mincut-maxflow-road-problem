from collections import defaultdict

class Graph:
  
    def __init__(self,graph):
        self.graph=graph
        self.org_graph=[i[:] for i in graph]
        self.ROW=len(graph)
        self.COL=len(graph[0])
         
    def BFS(self,s, t, parent):

        visited =[False]*(self.ROW)

        queue=[]

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def FordFulkerson(self, source, sink):

        parent = [-1]*(self.ROW)
 
        max_flow = 0

        while self.BFS(source, sink, parent) :
 
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow +=  path_flow

            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow



    def minCut(self, source, sink):
 
        parent=[-1]*(self.ROW)
        max_flow=0

        while self.BFS(source,sink,parent) :

            path_flow=float("Inf")
            s=sink
            while(s!=source):
                path_flow=min (path_flow,self.graph[parent[s]][s])
                s=parent[s]
 
            max_flow+=path_flow
            v=sink
            
            while(v!=source):
                u=parent[v]
                self.graph[u][v]-=path_flow
                self.graph[v][u]+=path_flow
                v=parent[v]
 
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j]==0 and self.org_graph[i][j]>0:
                    print(str(i)+" - "+str(j))


graph = [[0,6,10,4,0,0,0],
         [6,0,5,0,0,0,12],
         [10,5,0,0,3,7,0],
         [4,0,0,0,8,0,0],
         [0,0,3,8,0,0,0],
         [0,0,7,0,0,0,13],
         [0,12,0,0,0,13,0]]


g=Graph(graph)
 
source=0
destination=4

print("Source : ",source,"\t destination : ",destination,"\n")
print ("The maximum possible flow between locations  ",source," and ",destination," is ", g.FordFulkerson(source,destination))
print("\n")
print("The minimum cut has to be through:")
g.minCut(source,destination)

