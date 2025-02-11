'''
Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must prefer the left child over the right child when traversing. Do not include leaf nodes in this section.

Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.

Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, traversed in reverse order. You must prefer the right child over the left child when traversing. Do not include the root in this section if it was already included in the left boundary.

Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

Examples:

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
Output: [1, 2, 4, 8, 9, 6, 7, 3]
Explanation:

Input: root[] = [1, 2, N, 4, 9, 6, 5, N, 3, N, N, N, N 7, 8]
Output: [1, 2, 4, 6, 5, 7, 8]
Explanation:












As the root doesn't have a right subtree, the right boundary is not included in the traversal.
Input: root[] = [1, N, 2, N, 3, N, 4, N, N] 
    1
     \
      2
       \
        3
         \
          4

Output: [1, 4, 3, 2]
Explanation:
Left boundary: [1] (as there is no left subtree)
Leaf nodes: [4]
Right boundary: [3, 2] (in reverse order)
Final traversal: [1, 4, 3, 2]
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105

'''

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
            
        b=[]
        
        def lb(node):
            while node:
                if not isLeaf(node):
                    b.append(node.data)
                node=node.left if node.left else node.right
                
        def al(node):
            if node:
                al(node.left)
                if isLeaf(node):
                    b.append(node.data)
                al(node.right)
                
        def rb(node):
            stack=[]
            while node:
                if not isLeaf(node):
                    stack.append(node.data)
                node=node.right if node.right else node.left
            while stack:
                b.append(stack.pop())
                
        def isLeaf(node):
            return not node.left and not node.right
            
        self.isLeaf=isLeaf
        
        if not isLeaf(root):
            b.append(root.data)
            
        if root.left:
            lb(root.left)
            
        al(root)
        
        if root.right:
            rb(root.right)
            
        return b