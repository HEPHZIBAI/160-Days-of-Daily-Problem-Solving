'''
There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have prerequisites[][] tasks, for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m. Find a ordering of tasks you should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return any one of them. If it is impossible to finish all tasks, return an empty array. Returning any correct order will give the output as true, whereas any invalid order will give the output false. 

Examples:

Input: n = 2, prerequisites[][] = [[1, 0]]
Output: true
Explanation: Only possible order is [0, 1].
Input: n = 4, prerequisites[][] = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: true
Explanation: There are a total of 4 tasks to pick. To pick task 3 you should have finished both tasks 1 and 2. Both tasks 1 and 2 should be pick after you finished task 0. So one correct task order is [0, 1, 2, 3]. Another correct ordering is [0, 2, 1, 3]. Returning any of these order will result in an output of true.
Constraints:
1 ≤ n ≤ 105
0 ≤ prerequisites[i][0], prerequisites[i][1] < n
All prerequisite pairs are unique
prerequisites[i][0] ≠ prerequisites[i][1]
'''
class Solution:
    def dfs(self,n,a,v,s):
        v[n]=1
        
        for i in a[n]:
            if v[i]==1:
                return False
                
            elif v[i]==0:
                if not self.dfs(i,a,v,s):
                    return False
                    
        
        v[n]=2
        s.append(n)
        return True

    
    def findOrder(self, n, prerequisites):
        adj=[[] for _ in range(n)]
        
        for i in prerequisites:
            d,s=i
            adj[s].append(d)
            
        v=[0]*n
        stack=[]
        
        for i in range(n):
            if v[i]==0:
                if not self.dfs(i,adj,v,stack):
                    return []
                    
        stack.reverse()
        return stack

