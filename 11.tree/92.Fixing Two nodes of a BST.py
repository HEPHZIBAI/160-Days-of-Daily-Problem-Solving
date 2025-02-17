'''
Given the root of a Binary search tree(BST), where exactly two nodes were swapped by mistake. Your task is to fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original linked list.
 
Examples :
Input: root = [10, 5, 8, 2, 20]
     
Output: 1
       

Explanation: The nodes 20 and 8 were swapped. 
Input: root = [5, 10, 20, 2, 8]
     
Output: 1 
     
Explanation: The nodes 10 and 5 were swapped.
Constraints:
1 ≤ Number of nodes ≤ 103

'''

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def correctBST(self, root):
        f=s=p=None
        
        def inorder(node):
            nonlocal f,s,p
            
            if not node:
                return
            
            inorder(node.left)
            
            if p and p.data>node.data:
                if not f:
                    f=p
                s=node
                
            p=node
            inorder(node.right)
            
        inorder(root)
        
        if f and s:
            f.data,s.data=s.data,f.data
            
        return 1