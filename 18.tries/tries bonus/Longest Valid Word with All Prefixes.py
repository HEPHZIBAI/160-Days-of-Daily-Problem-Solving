'''
Given an array of strings words[], find the longest string such that every prefix of it is also present in words[]. If multiple strings have the same maximum length, return the lexicographically smallest one.

If no such string is found, return an empty string.

Examples:

Input: words[] = ["p", "pr", "pro", "probl", "problem", "pros", "process", "processor"]
Output: "pros" 
Explanation: "pros" is the longest word with all prefixes ("p", "pr", "pro", "pros") present.
Input: words[] = ["geeks", "gfg", "geeksforgeeks"]
Output: ""
Explanation: No valid strings for all their prefixes present in the words array.
Constraints:
1 <= words.size <= 1000
1 <= words[i].size <= 100
'''


class Node:
    def __init__(self):
        self.children=[None]*26
        self.eow=False

class Solution:
    def insert(self,root,s):
        curr=root
        
        for i in s:
            idx=ord(i)-ord('a')
            
            if curr.children[idx] is None:
                curr.children[idx]=Node()
                
            curr=curr.children[idx]
            
        curr.eow=True
    
    def lsr(self,root,pre):
        if root is None:
            return pre
            
        l=pre
        
        for i in range(26):
            if root.children[i] is not None and root.children[i].eow:
                s=pre+chr(i+ord('a'))
                curr=self.lsr(root.children[i],s)
                
                if len(curr)>len(l):
                    l=curr
                    
        return l
    
    def longestValidWord(self, words):
        root=Node()
        
        for i in words:
            self.insert(root,i)
            
        return self.lsr(root,"")
            
