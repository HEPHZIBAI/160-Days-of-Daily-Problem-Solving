'''
You are given a binary tree with n nodes, where each node contains a certain number of candies, and the total number of candies across all nodes is n. In one move, we can select two adjacent nodes and transfer one candy from one node to the other. The transfer can occur between a parent and child in either direction.

The task is to determine the minimum number of moves required to ensure that every node in the tree has exactly one candy.

Note: The testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy, after some moves.

Examples:

Input: root[] = [3, 0, 0]
        
Output: 2
Explanation: From the root of the tree, we move one candy to its left child, and one candy to its right child. 
Input: root[] = [0, 3, 0]
         
Output: 3
Explanation: From the left child of the root, we move two candies to the root [taking two moves]. Then, we move one candy from the root of the tree to the right child.
Constraints:
1 <= n <= 104
0 <= Node->data <= n
The sum of all Node->data is equal to n




'''



class Solution:
    def distributeCandy(self, root):
        if root is None:
            return 0
            
        ans=0
        stk=[]
        balance={}
        stk.append((root,0))
        
        while stk:
            curr=stk.pop()
            node=curr[0]
            state=curr[1]
            
            if node is None:
                continue
            
            if state==0:
                stk.append((node,1))
                stk.append((node.left,0))
                stk.append((node.right,0))
            else:
                lb=balance.get(node.left,0)
                rb=balance.get(node.right,0)
                ans+=abs(lb)+abs(rb)
                balance[node]=node.data+lb+rb-1
                
        return ans