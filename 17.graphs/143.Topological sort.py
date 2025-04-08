'''
Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes an directed edge u -> v. Return topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false.

Examples:

Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
Input: V = 6, E = 6, edges[][] = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the graph are:
[4, 5, 0, 1, 2, 3]
[5, 2, 4, 0, 1, 3]
Constraints:
2  ≤  V  ≤  103
1  ≤  E = edges.size()  ≤  (V * (V - 1)) / 2

'''



from collections import deque
class Solution:
    
    def topoSort(self, V, edges):
        adj=[[] for _ in range(V)]
        ind=[0]*V
        
        for u,v in edges:
            adj[u].append(v)
            ind[v]+=1
            
        queue=deque()
        for i in range(V):
            if ind[i]==0:
                queue.append(i)
                
        to=[]
        
        while queue:
            node=queue.popleft()
            to.append(node)
            
            for i in adj[node]:
                ind[i]-=1
                if ind[i]==0:
                    queue.append(i)
                    
        return to if len(to)==V else []