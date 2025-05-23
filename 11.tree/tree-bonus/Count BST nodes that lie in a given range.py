'''
Given a Binary Search Tree (BST) and a range l-h (inclusive), your task is to return the number of nodes in the BST whose value lie in the given range.

Examples :

Input: root[] = [10, 5, 50, 1, N, 40, 100], l = 5, h = 45
         
Output: 3
Explanation: There are three nodes in range [5, 45] =  5, 10 and 40.
Input: root[] = [10, 5, 50, 1, N, 40, 100], l = 10, h = 100
         
Output: 4
Explanation: There are four nodes in range [10, 100] = 10, 40, 50 and 100.
Input: root[] = [1, 2, 3], l = 23, h = 95
         
Output: 0
Explanation: There are no nodes in range [23, 95].
Constraints:
1 <= Number of nodes <= 105
1 <= l <= h < =105
'''

class Solution:
    def getCount(self, root, l, h):
        if root is None:
            return 0
            
        q=deque([root])
        ans=0
        
        while q:
            curr=q.popleft()
            if l<=curr.data<=h:
                ans+=1
                if curr.left is not None:
                    q.append(curr.left)
                    
                if curr.right is not None:
                    q.append(curr.right)
                    
            elif curr.data<l:
                if curr.right is not None:
                    q.append(curr.right)
                    
            else:
                if curr.left is not None:
                    q.append(curr.left)
                    
        return ans