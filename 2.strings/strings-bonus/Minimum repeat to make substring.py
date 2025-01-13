'''
Given two strings s1 and s2. Return a minimum number of times s1 has to be repeated such that s2 is a substring of it. If s2 can never be a substring then return -1.

Note: Both the strings contain only lowercase letters.

Examples:

Input: s1 = "ww", s2 = "www"
Output: 2
Explanation: Repeating s1 two times "wwww", s2 is a substring of it.
Input: s1 = "abcd", s2 = "cdabcdab" 
Output: 3 
Explanation: Repeating s1 three times "abcdabcdabcd", s2 is a substring of it. s2 is not a substring of s1 when it is repeated less than 3 times.
Input: s1 = "ab", s2 = "cab"
Output: -1
Explanation: No matter how many times we repeat s1, we can't get a string such that s2 is a substring of it.
Constraints:
1 ≤ s1.size(), s2.size() ≤ 105
'''
class Solution:
    def cpa(self,s):
        lps=[0]*len(s)
        len_=0
        idx=1
        
        while idx<len(s):
            if s[idx]==s[len_]:
                len_+=1
                lps[idx]=len_
                idx+=1
            else:
                if len_==0:
                    lps[idx]=0
                    idx+=1
                else:
                    len_=lps[len_-1]
        return lps
    
    def kmp(self,text,pat,lps):
        n,m=len(text),len(pat)
        i=j=0
        
        while i<n:
            if text[i]==pat[j]:
                i+=1
                j+=1
                if j==m:
                    return True
                    j=lps[j-1]
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return False
    
    def minRepeats(self, s1, s2):
        n,m=len(s1),len(s2)
        lps=self.cpa(s2)
        x=(m+n-1)//n
        text=s1*x
        
        if self.kmp(text,s2,lps):
            return x
        
        text+=s1
        
        if self.kmp(text,s2,lps):
            return x+1
            
        return -1