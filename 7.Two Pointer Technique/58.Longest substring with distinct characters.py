'''
Given a string s, find the length of the longest substring with all distinct characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.
Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.
Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.
Constraints:
1<= s.size()<=3*104
All the characters are in lowercase.
'''

class Solution:
    def longestUniqueSubstr(self, s):
        if not s:
            return 0
            
        ml=0
        l=0
        ciw=set()
        
        for r in range(len(s)):
            while s[r] in ciw:
                ciw.remove(s[l])
                l+=1
            ciw.add(s[r])
            ml=max(ml,r-l+1)
        return ml