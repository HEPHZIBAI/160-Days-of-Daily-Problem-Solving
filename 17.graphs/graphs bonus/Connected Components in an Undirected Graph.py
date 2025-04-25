'''
Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented as a 2D array edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v.

Your task is to return a list of all connected components. Each connected component should be represented as a list of its vertices, with all components returned in a collection where each component is listed separately.

Note: You can return the components in any order, driver code will print the components in sorted order.

Examples :

Input: V = 5, edges[][] = [[0, 1], [2, 1], [3, 4]]
Output: [[0, 1, 2], [3, 4]]
Explanation:

Input: V = 7, edges[][] = [[0, 1], [6, 0], [2, 4], [2, 3], [3, 4]]
Output: [[0, 1, 6], [2, 3, 4], [5]]
Explanation:

Constraints:
1 ≤ V ≤ 105
1 ≤ edges.size() ≤ 105
0 <= edges[i][0], edges[i][1] < V
'''


class Solution:
    def fp(self,p,x):
        if p[x]==x:
            return x
            
        p[x]=self.fp(p,p[x])
        return p[x]
        
    def us(self,p,x,y):
        px=self.fp(p,x)
        py=self.fp(p,y)
        
        if px!=py:
            p[px]=py
    
    def getComponents(self, V, edges):
        p=[i for i in range(V)]
        
        for i in edges:
            self.us(p,i[0],i[1])
            
        for i in range(V):
            p[i]=self.fp(p,i)
            
        rm={}
        
        for i in range(V):
            r=p[i]
            if r not in rm:
                rm[r]=[]
            rm[r].append(i)
            
        return list(rm.values())