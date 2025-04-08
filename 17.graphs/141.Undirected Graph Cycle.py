'''
Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Examples:

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
Explanation: 
 
1 -> 2 -> 0 -> 1 is a cycle.
Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
Output: false
Explanation: 
 
No cycle in the graph.
Constraints:
1 ≤ V ≤ 105
1 ≤ E = edges.size() ≤ 105


'''
class Solution:
	def isCycle(self, V, edges):
		from collections import defaultdict
		
		adj=defaultdict(list)
		
		for u,v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		    
		visited=[False]*V
		
		def dfs(node,parent):
		    visited[node]=True
		    
		    for i in adj[node]:
		        if not visited[i]:
		            if dfs(i,node):
		                return True
		        elif i!=parent:
		            return True
		            
		    return False
		    
		for i in range(V):
		     if not visited[i]:
		         if dfs(i,-1):
		             return True
		return False
