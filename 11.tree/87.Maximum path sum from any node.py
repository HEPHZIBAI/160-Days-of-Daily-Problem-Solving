'''
Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

Examples:

Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
Output: 42
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Input: root[] = [-17, 11, 4, 20, -2, 10]
Output: 31
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Constraints:
1 ≤ number of nodes ≤ 103
-104 ≤ node->data ≤ 104


'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        self.max_sum=float('-inf')
        
        def dfs(node):
            if not node:
                return 0
                
            lm=max(0,dfs(node.left))
            rm=max(0,dfs(node.right))
            self.max_sum=max(self.max_sum,lm+rm+node.data)
            return max(lm,rm)+node.data
        dfs(root)
        return self.max_sum
