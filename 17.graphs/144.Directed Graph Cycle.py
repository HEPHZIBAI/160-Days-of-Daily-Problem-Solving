'''

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v.

Examples:

Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 3], [3, 3]]



Output: true
Explanation: 3 -> 3 is a cycle
Input: V = 3, edges[][] = [[0, 1], [1, 2]]



Output: false
Explanation: no cycle in the graph
Constraints:
1 ≤ V, E ≤ 105



'''

class Solution:
    def isCycle(self, V, edges):
        from collections import defaultdict
        
        graph=defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            
        v=[False]*V
        r=[False]*V
        
        def dfs(node):
            v[node]=True
            r[node]=True
            
            for i in graph[node]:
                if not v[i]:
                    if dfs(i):
                        return True
                elif r[i]:
                    return True
                    
            r[node]=False
            return False
            
        for i in range(V):
            if not v[i]:
                if dfs(i):
                    return True
                    
        return False

