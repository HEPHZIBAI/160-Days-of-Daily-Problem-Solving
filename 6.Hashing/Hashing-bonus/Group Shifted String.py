'''
Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group are shifted versions of each other.

Two strings s1 and s2 are called shifted if the following conditions are satisfied:

s1.length = s2.length
s1[i] = s2[i] + m for 1 <= i <= s1.length  for a constant integer m
Examples :

Input: arr = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
Output: [["acd", "dfg", "wyz", "yab", "mop"], ["bdfh", "moqs"], ["a", "x"]] 
Explanation: All shifted strings are grouped together.
Input: arr = ["geek", "for", "geeks"]
Output: [["for"], ["geek"], ["geeks"]]
Input: arr = ["aaa", "adb", "bbd", "dbc", "bca"]
Output: [["aaa"], ["adb"], ["bbd"], ["bca"], ["dbc"]]
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i].size() ≤ 5

'''

class Solution:
    def gh(self,s):
        sh=ord(s[0])-ord('a')
        hv=[]
        
        for i in s:
            nc=chr(ord(i)-sh)
            
            if nc<'a':
                nc=chr(ord(nc)+26)
            hv.append(nc)
        return ''.join(hv)
    
    def groupShiftedString(self, arr):
        res=[]
        mp={}
        
        for s in arr:
            hv=self.gh(s)
            
            if hv not in mp:
                mp[hv]=len(res)
                res.append([])
            
            res[mp[hv]].append(s)
        return res