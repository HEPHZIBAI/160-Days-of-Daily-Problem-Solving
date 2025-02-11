'''
Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: 2
Explanation: The longest path has 2 edges (node 2 -> node 1 -> node 3).

Input: root[] = [5, 8, 6, 3, 7, 9]

Output: 4
Explanation: The longest path has 4 edges (node 3 -> node 8 -> node 5 -> node 6 -> node 9).

Constraints:
1 ≤ number of nodes ≤ 105
0 ≤ node->data ≤ 105

'''
class Solution:
    def diameter(self, root):
        self.md=0
        
        def height(node):
            if not node:
                return 0
                
            lh=height(node.left)
            rh=height(node.right)
            self.md=max(self.md,lh+rh)
            
            return 1+max(lh,rh)
            
        height(root)
        return self.md
