'''
Given a string s, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of the given string.

Examples:

Input: s = "geek" 
Output: 2 
Explanation: We need to make minimum 2 cuts, i.e., "g | ee | k".
Input: s = "aaaa" 
Output: 0
Explanation: The string is already a palindrome.
Input: s = "ababbbabbababa" 
Output: 3
Explanation: We need to make minimum 3 cuts, i.e., "aba | bb | babbab | aba".
Constraints:
1 ≤ |s| ≤ 103
s contain lowercase letters only


'''

class Solution:
    def gen(self,s,ispalin):
        n=len(s)
        
        for i in range(n):
            ispalin[i][i]=True
            
        for i in range(2,n+1):
            for j in range(n-i+1):
                k=j+i-1
                
                if s[j]==s[k] and (i==2 or ispalin[j+1][k-1]):
                    ispalin[j][k]=True
                    
    
    def palPartition(self, s):
        n=len(s)
        ispalin=[[False]*n for _ in range(n)]
        self.gen(s,ispalin)
        dp=[n]*n
        dp[0]=0
        for i in range(1,n):
            if ispalin[0][i]:
                dp[i]=0
            else:
                for j in range(i,0,-1):
                    if ispalin[j][i]:
                        dp[i]=min(dp[i],1+dp[j-1])
                        
        return dp[n-1]