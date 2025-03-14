'''
Given a root of a binary tree with n nodes, the task is to find its level order traversal. Level order traversal of a tree is breadth-first traversal for the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: [[1], [2, 3]]
Input: root[] = [10, 20, 30, 40, 50]

Output: [[10], [20, 30], [40, 50]]
Input: root[] = [1, 3, 2, N, N, N, 4, 6, 5]

Output: [[1], [3, 2], [4], [6, 5]]
Constraints:

1 ≤ number of nodes ≤ 105
0 ≤ node->data ≤ 109
'''


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
            
        result=[]
        q=deque([root])
        
        while q:
            ls=len(q)
            l=[]
            
            for i in range(ls):
                node=q.popleft()
                l.append(node.data)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
            result.append(l)
            
        return result