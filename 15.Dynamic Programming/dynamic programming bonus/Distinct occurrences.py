'''
You are given two strings txt and pat, find the count of distinct occurrences of pat as a subsequence in txt.

Examples:

Input: txt = "abba", pat = "aba"
Output: 2
Explanation: There are 3 sub-sequences: [abba], [abba].
Input: txt = "banana", pat = "ban"
Output: 3
Explanation: There are 3 sub-sequences: [banana], [banana], [banana].
Constraints:
1 ≤ txt.size() ≤ pat.size() ≤ 103
Both txt and pat contain only lowercase alphabets.

'''


class Solution:
    def subseqCount(self, txt, pat):
        m,n=len(pat),len(txt)
        
        if m>n:
            return 0
            
        p=[0]*(m+1)
        c=[0]*(m+1)
        
        p[0]=1
        
        for i in range(1,n+1):
            c[0]=1
            for j in range(1,m+1):
                if txt[i-1]==pat[j-1]:
                    c[j]=p[j-1]+p[j]
                else:
                    c[j]=p[j]
                    
            p=c.copy()
        return p[m]