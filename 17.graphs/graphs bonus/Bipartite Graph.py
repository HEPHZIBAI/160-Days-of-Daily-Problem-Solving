'''
Given a Graph with V vertices (Numbered from 0 to V-1) and E edges. Check whether the graph is bipartite or not.

A bipartite graph can be colored with two colors such that no two adjacent vertices share the same color. This means we can divide the graph’s vertices into two distinct sets where:

All edges connect vertices from one set to vertices in the other set.
No edges exist between vertices within the same set.
Examples:

Input: V = 3, edges[][] = [[0, 1], [1,2]]
Bipartite-Graph
Output: true
Explanation: The given graph can be colored in two colors so, it is a bipartite graph.
Input: V = 4, edges[][] = [[0, 3], [1, 2], [3, 2], [0, 2]]




Output: false 
Explanation: The given graph cannot be colored in two colors such that color of adjacent vertices differs. 
Constraints:
1 ≤ V ≤ 2 * 105
1 ≤ edges.size() ≤ 105
1 ≤ edges[i][j] ≤ 105



'''


#User function Template for python3
from collections import deque

class Solution:
    def ca(self,v,e):
        a=[[] for _ in range(v)]
        for u,v in e:
            a[u].append(v)
            a[v].append(u)
        return a
    
    def isBipartite(self, V, edges):
        c=[-1]*V
        a=self.ca(V,edges)
        
        for i in range(V):
            if c[i]==-1:
                c[i]=0
                q=deque([i])
                
                while q:
                    u=q.popleft()
                    
                    for v in a[u]:
                        if c[v]==-1:
                            c[v]=1-c[u]
                            q.append(v)
                        elif c[v]==c[u]:
                            return False
                            
        return True