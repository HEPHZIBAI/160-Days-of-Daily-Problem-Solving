'''
Given a root of a Binary Search Tree, modify and return the given BST such that it is balanced and has minimum possible height. If there is more than one answer, return any of them.

Note: The height of balanced BST returned by you will be compared with the expected height of the balanced tree.

Examples:

Input: root[] = [30, 20, N, 10, N]
     
Output: 2
     
Explanation: The above unbalanced BST is converted to balanced with the minimum possible height i.e. 2.
Input: root[] = [4, 3, 5, 2, N, N, 6, 1, N, N, 7]
     
Output: 3
     
Explanation: The above unbalanced BST is converted to balanced with the minimum possible height i.e. 3.
Constraints:
1 <= Number of Nodes <= 105
1 <= Node -> data <= 109

'''


class Solution:
    def storeInorder(self,root,nodes):
        if root is None:
            return
        
        self.storeInorder(root.left,nodes)
        nodes.append(root.data)
        self.storeInorder(root.right,nodes)
    
    def bbt(self,nodes,start,end):
        if start>end:
            return None
            
        mid=(start+end)//2
        root=Node(nodes[mid])
        root.left=self.bbt(nodes,start,mid-1)
        root.right=self.bbt(nodes,mid+1,end)
        return root
        
    
    def balanceBST(self,root):
        nodes=[]
        self.storeInorder(root,nodes)
        return self.bbt(nodes,0,len(nodes)-1)
