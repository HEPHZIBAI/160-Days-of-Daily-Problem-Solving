'''
Geek has successfully developed an effective vaccine for the Coronavirus and aims to ensure that every house in Geek Land has access to it. The houses in Geek Land are structured as a binary tree, where each node represents a house, and the edges denote direct connections between houses.

Each house that receives a vaccine kit can provide coverage to:

Itself
Its direct parent house (if it exists)
Its immediate child houses (if any exist)
Your task is to determine the minimum number of houses that must be supplied with a vaccine kit to ensure that every house is covered.

Examples:

Input: root = [1, 2, 3, N, N, N, 4, N, 5, N, 6]


Output: 2
Explanation: The vaccine kits should be supplied to house numbers 1 and 5.
Input: root = [1, 2, 3]

Output: 1
Explanation: The vaccine kits should be supplied to house number 1.
Constraints:
1 ≤ number of nodes ≤ 105

1 ≤  node->data  ≤ 105



'''


class Solution:
    def mv(self,root,res):
        if not root:
            return 1
            
        l=self.mv(root.left,res)
        r=self.mv(root.right,res)
        
        if l==0 or r==0:
            res[0]+=1
            return 2
            
        if l==2 or r==2:
            return 1
            
        return 0
    
    def supplyVaccine(self, root):
        res=[0]
        
        if self.mv(root,res)==0:
            res[0]+=1
            
        return res[0]
