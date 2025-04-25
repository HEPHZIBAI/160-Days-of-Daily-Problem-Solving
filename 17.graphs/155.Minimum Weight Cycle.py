'''
Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by a 2d array edges[][], where edges[i] = [u, v, w] represents the edge between the nodes u and v having w edge weight.
Your task is to find the minimum weight cycle in this graph.

Examples:

Input: V = 5, edges[][] = [[0, 1, 2], [1, 2, 2], [1, 3, 1], [1, 4, 1], [0, 4, 3], [2, 3, 4]]

Output: 6
Explanation: 

Minimum-weighted cycle is  0 → 1 → 4 → 0 with a total weight of 6(2 + 1 + 3)
Input: V = 5, edges[][] = [[0, 1, 3], [1, 2, 2], [0, 4, 1], [1, 4, 2], [1, 3, 1], [3, 4, 2], [2, 3, 3]]

Output: 5
Explanation: 

Minimum-weighted cycle is  1 → 3 → 4 → 1 with a total weight of 5(1 + 2 + 2)
Constraints:
1 ≤ V ≤ 100
1 ≤ E = edges.size() ≤ 103 
1 ≤ edges[i][j] ≤ 100
'''


class Solution:
    def dijkstra(self,V,adj,src):
        dist=[sys.maxsize]*V
        dist[src]=0
        pq=[(0,src)]
        
        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            
            for n,w in adj[node]:
                nd=d+w
                
                if nd<dist[n]:
                    dist[n]=nd
                    heapq.heappush(pq,(nd,n))
                    
        return dist
    
    def findMinCycle(self, V, edges):
        adj=[[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        mc=sys.maxsize
        
        for u,v,w in edges:
            adj[u]=[x for x in adj[u] if x[0]!=v]
            adj[v]=[x for x in adj[v] if x[0]!=u]
            
            dfu=self.dijkstra(V,adj,u)
        
            if dfu[v] < sys.maxsize:
                cw=dfu[v]+w
                mc=min(mc,cw)
                
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        return mc if mc!=sys.maxsize else -1
        
