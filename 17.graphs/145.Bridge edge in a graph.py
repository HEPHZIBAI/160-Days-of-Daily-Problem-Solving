'''

Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u,v] represents the edge between the vertices u and v. Determine whether a specific edge between two vertices (c, d) is a bridge.

Note:

An edge is called a bridge if removing it increases the number of connected components of the graph.
if there’s only one path between c and d (which is the edge itself), then that edge is a bridge.
Examples :

Input:

c = 1, d = 2
Output: true
Explanation: From the graph, we can clearly see that blocking the edge 1-2 will result in disconnection of the graph.
Hence, it is a Bridge.
Input:

c = 0, d = 2
Output: false
Explanation:

Blocking the edge between nodes 0 and 2 won't affect the connectivity of the graph.
So, it's not a Bridge Edge. All the Bridge Edges in the graph are marked with a blue line in the above image.
Constraints:
1 ≤ V, E ≤ 105
0 ≤ c, d ≤ V-1

'''
class Solution:
    def isBridge(self, V, edges, c, d):
        disc=[-1]*V
        low=[-1]*V
        t=[0]
        found=[False]
        
        adj=[[] for _ in range(V)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(u,p):
            disc[u]=low[u]=t[0]
            t[0]+=1
            
            for v in adj[u]:
                if v==p:
                    continue
                
                if disc[v]==-1:
                    dfs(v,u)
                    low[u]=min(low[u],low[v])
                    
                    if low[v]>disc[u]:
                        if (u==c and v==d) or (u==d and v==c):
                            found[0]=True
                else:
                    low[u]=min(low[u],disc[v])
                    
        for i in range(V):
            if disc[i]==-1:
                dfs(i,-1)
                
        return found[0]
