'''
Given a binary tree, determine if it is height-balanced. A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree.

Examples:

Input: root[] = [10, 20, 30, 40, 60]

   
Output: true
Explanation: The height difference between the left and right subtrees at all nodes is at most 1. Hence, the tree is balanced.
Input: root[] = [1, 2, 3, 4, N, N, N, 5]
   
Output: false
Explanation: The height difference between the left and right subtrees at node 2 is 2, which exceeds 1. Hence, the tree is not balanced.
Input: root[] = [1, 2, N, N, 3]
   
Output: false
Explanation: The height difference between the left and right subtrees at node 1 is 2, which exceeds 1. Hence, the tree is not balanced.
Constraints:
0 <= number of nodes <= 5000
- 104 <= node->data <= 104

'''
class Solution:
    def isBalanced(self, root):
        return self.checkHeight(root)!=-1
        
    def checkHeight(self,node):
        if not node:
            return 0
            
        lh=self.checkHeight(node.left)
        if lh==-1:
            return -1
            
        rh=self.checkHeight(node.right)
        
        if rh==-1:
            return -1
            
        if abs(lh-rh)>1:
            return -1
        
        return max(lh,rh)+1

