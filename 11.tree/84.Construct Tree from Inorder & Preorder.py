'''

Given two arrays representing the inorder and preorder traversals of a binary tree, construct the tree and return the root node of the constructed tree.

Note: The output is written in postorder traversal.

Examples:

Input: inorder[] = [1, 6, 8, 7], preorder[] = [1, 6, 7, 8]
Output: [8, 7, 6, 1]
Explanation: The tree will look like

Input: inorder[] = [3, 1, 4, 0, 2, 5], preorder[] = [0, 1, 3, 4, 2, 5]
Output: [3, 4, 1, 5, 2, 0]
Explanation: The tree will look like

Input: inorder[] = [2, 5, 4, 1, 3], preorder[] = [1, 4, 5, 2, 3]
Output: [2, 5, 4, 3, 1]
Explanation: The tree will look like

Constraints:
1 ≤ number of nodes ≤ 103
0 ≤ nodes -> data ≤ 103
Both the inorder and preorder arrays contain unique values.


'''
class Solution:
    def bth(self,io,po,im,pi,iss,ie):
        if iss>ie:
            return None
            
        rv=po[pi[0]]
        r=Node(rv)
        pi[0]+=1
        ii=im[rv]
        r.left=self.bth(io,po,im,pi,iss,ii-1)
        r.right=self.bth(io,po,im,pi,ii+1,ie)
        
        return r
        
    
    def buildTree(self, inorder, preorder):
        im={val:idx for idx , val in enumerate(inorder)}
        pi=[0]
        return self.bth(inorder,preorder,im,pi,0,len(inorder)-1)