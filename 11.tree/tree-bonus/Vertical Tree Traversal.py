'''
Given a root of a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

Examples:

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, N, N, N, 8, N, 9]
     Vertical-Taversal-          
Output: [[4], [2], [1, 5, 6], [3, 8], [7], [9]]
Explanation: The below image shows the horizontal distances used to print vertical traversal starting from the leftmost level to the rightmost level.
     
Input: root[] = [1, 2, 3, 4, 5, N, 6]
     
Output: [[4], [2], [1, 5], [3], [6]]
Explanation: From left to right the vertical order will be [[4], [2], [1, 5], [3], [6]]
Constraints:
1 <= number of nodes <= 105
1 <= node->data <= 105

'''



from collections import defaultdict,deque


class Solution:
    
    def dfs(self,root,hd,mn,mp):
        if root is None:
            return
        
        if hd not in mp:
            mp[hd]=[]
            
        mp[hd].append(root.data)
        mn[0]=min(mn[0],hd)
        self.dfs(root.left,hd-1,mn,mp)
        self.dfs(root.right,hd+1,mn,mp)
    
    def verticalOrder(self, root): 
        mp={}
        mn=[0]
        self.dfs(root,0,mn,mp)
        res=[]
        hd=mn[0]
        
        while hd in mp:
            res.append(mp[hd])
            hd+=1
            
        return res