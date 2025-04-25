'''
Given an array arr[] of non-negative integers of size n. Find the maximum possible XOR between two numbers present in the array.

Examples:

Input: arr[] = [25, 10, 2, 8, 5, 3]
Output: 28
Explanation: The maximum possible XOR is 5 ^ 25 = 28.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7]
Output: 7
Explanation : The maximum possible XOR is 1 ^ 6 = 7.
Constraints:
2 ≤ arr.size() ≤ 5*104
1 ≤ arr[i] ≤ 106


'''


class TrieNode:
    def __init__(self):
        self.children={}

class Solution:
    def insert(self,root,num):
        node=root
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if bit not in node.children:
                node.children[bit]=TrieNode()
            node=node.children[bit]
            
    def fmxw(self,root,num):
        node=root
        mx=0
        
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            tb=1-bit
            
            if tb in node.children:
                mx|=(1<<i)
                node=node.children[tb]
            else:
                node=node.children.get(bit,node)
                
        return mx
    
    def maxXor(self, arr):
        root=TrieNode()
        mx=0
        
        for i in arr:
            self.insert(root,i)
            
        for i in arr:
            mx=max(mx,self.fmxw(root,i))
            
        return mx