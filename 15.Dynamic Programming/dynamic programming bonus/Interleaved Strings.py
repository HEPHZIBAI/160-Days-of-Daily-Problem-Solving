'''

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
Interleaving of two strings s1 and s2 is a way to mix their characters to form a new string s3, while maintaining the relative order of characters from s1 and s2. Conditions for interleaving:

Characters from s1 must appear in the same order in s3 as they are in s1.
Characters from s2 must appear in the same order in s3 as they are in s2.
The length of s3 must be equal to the combined length of s1 and s2.
Examples :

Input: s1 = "AAB", s2 = "AAC", s3 = "AAAABC", 
Output: true
Explanation: The string "AAAABC" has all characters of the other two strings and in the same order.
Input: s1 = "AB", s2 = "C", s3 = "ACB", 
Output: true
Explanation: s3 has all characters of s1 and s2 and retains order of characters of s1.
Input: s1 = "YX", s2 = "X", s3 = "XXY"
Output: false
Explanation: "XXY " is not interleaved of "YX" and "X". The strings that can be formed are YXX and XYX
Constraints:
1 ≤ s1.length, s2.length ≤ 300
1 ≤ s3.length ≤ 600


'''

class Solution:
    def isInterleave(self, s1, s2, s3):
        m=len(s1)
        n=len(s2)
        
        if m+n!=len(s3):
            return False
            
        dp=[[False] * (n+1) for _ in range(m+1)]
        dp[0][0]=True
        
        for j in range(1,n+1):
            dp[0][j]=(s3[j-1]==s3[j-1]) and dp[0][j-1]
            
        for i in range(1,m+1):
            dp[i][0]=(s1[i-1]==s3[i-1]) and dp[i-1][0]
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                k=i+j
                dp[i][j]=(s1[i-1]==s3[k-1] and dp[i-1][j]) or (s2[j-1]==s3[k-1] and dp[i][j-1])

        return dp[m][n]