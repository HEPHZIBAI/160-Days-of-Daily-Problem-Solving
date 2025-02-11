'''
Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. A path can start and end at any node within the tree but must always move downward (from parent to child).

Examples:

Input: k = 7   

Output: 3
Explanation: The following paths sum to k 
 
Input: k = 3

Output: 2
Explanation:
Path 1 : 1 -> 2 (Sum = 3)
Path 2 : 3 (Sum = 3)


Constraints:

1 ≤ number of nodes ≤ 104
-100 ≤ node value ≤ 100
-109 ≤ k ≤ 109

'''

from collections import defaultdict

class Solution:
    def sumK(self,root,k):
        def dfs(node,cs):
            nonlocal count
            
            if not node:
                return
            
            cs+=node.data
            count+=psc[cs-k]
            psc[cs]+=1
            
            dfs(node.left,cs)
            dfs(node.right,cs)
            
            psc[cs]-=1
            
        count=0
        psc=defaultdict(int)
        psc[0]=1
        dfs(root,0)
        return count