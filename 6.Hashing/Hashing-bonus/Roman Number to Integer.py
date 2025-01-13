'''
Given a string in Roman number format (s), your task is to convert it to an integer. Various symbols and their values are given below.
Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

Examples:

Input: s = "IX"
Output: 9
Explanation: IX is a Roman symbol which represents 10 – 1 = 9.
Input: s = "XL" 
Output: 40
Explanation: XL is a Roman symbol which represents 50 – 10 = 40.
Input: s = "MCMIV" 
Output: 1904
Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904.
Constraints:
1<= roman number <=3999
s[i] belongs to [I, V, X, L, C, D, M]
'''

class Solution:
    def romanToDecimal(self, s): 
        a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        h=0
        while i<len(s)-1:
            if a[s[i]]>=a[s[i+1]]:
                h+=a[s[i]]
            else:
                m=a[s[i]]
                i+=1
                n=a[s[i]]
                h+=(n-m)
            i+=1
            #print(h)
        if i<len(s):
            h+=a[s[i]]
        return h