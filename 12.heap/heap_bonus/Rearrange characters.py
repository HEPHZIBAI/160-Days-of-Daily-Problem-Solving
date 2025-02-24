'''
Given a string s with repeated characters, the task is to rearrange characters in a string such that no two adjacent characters are the same.
Note: The string has only lowercase English alphabets and it can have multiple solutions. Return any one of them. If there is no possible solution, then print empty string ("").

Examples:

Input : s = "aaabc"
Output: 1
Explanation: "aaabc" can rearranged to "abaca" or "acaba" as no two adjacent characters are same in the output string.
Input : s= "aaabb"
Output: 0
Explanation: No combinations possible such that two adjacent characters are different.
Input : s = "aaaabc"
Output: 0
Explanation: No combinations possible such that two adjacent characters are different.
Constraints :
1 <= s.size() <= 104


'''


import heapq
from collections import Counter

class Solution :
    def rearrangeString(self, s):
        freq=Counter(s)
        mf=max(freq.values())
        
        if mf>(len(s)+1)//2:
            return '0'
            
        mh=[(-count,char) for char,count in freq.items()]
        heapq.heapify(mh)
        result=[]
        pc,pch=0,''
        
        while mh:
            count,char=heapq.heappop(mh)
            result.append(char)
            
            if pc<0:
                heapq.heappush(mh,(pc,pch))
                
            pc,pch=count+1,char
        
        return result
