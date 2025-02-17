'''
Given a root of a Binary Tree. Your task is to check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself.

Examples:

Input: root[] = [1, 2, 2, 3, 4, 4, 3]
   ex-1_1
Output: True
Explanation: Tree is mirror image of itself i.e. tree is symmetric.
Input: root[] = [1, 2, 2, N, 3, N, 3]
   ex-2_1
Output: False
Explanation: Tree is not mirror image of itself i.e. tree is not symmetric.
Constraints:
1<= number of nodes<=2000

'''


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left,root.right)
        
    def isMirror(self,t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
            
        return(t1.data==t2.data and self.isMirror(t1.left,t2.right) and self.isMirror(t1.right,t2.left))
