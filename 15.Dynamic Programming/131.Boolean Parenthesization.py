'''
You are given a boolean expression s containing
    'T' ---> true
    'F' ---> false 
and following operators between symbols
   &   ---> boolean AND
    |   ---> boolean OR
   ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Note: The answer is guaranteed to fit within a 32-bit integer.

Examples:

Input: s = "T|T&F^T"
Output: 4
Explaination: The expression evaluates to true in 4 ways: ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).
Input: s = "T^F|F"
Output: 2
Explaination: The expression evaluates to true in 2 ways: ((T^F)|F) and (T^(F|F)).
Constraints:
1 ≤ |s| ≤ 100 

'''

class Solution:
    def countWays(self, s):
        dp={}
        
        def solve(i,j,isTrue):
            if i>j:
                return 0
                
            if i==j:
                return 1 if (s[i]=='T') == isTrue else 0
                
            if (i,j,isTrue) in dp:
                return dp[(i,j,isTrue)]
                
            ways=0
            
            for k in range(i+1,j,2):
                lt=solve(i,k-1,True)
                lf=solve(i,k-1,False)
                rt=solve(k+1,j,True)
                rf=solve(k+1,j,False)
                
                if s[k]=='&':
                    if isTrue:
                        ways+=lt*rt
                    else:
                        ways+=lf*rt+lt*rf+lf*rf
                        
                elif s[k]=='|':
                    if isTrue:
                        ways+=lt*rt+lt*rf+lf*rt
                    else:
                        ways+=lf*rf
                        
                elif s[k]=='^':
                    if isTrue:
                        ways+=lt*rf+lf*rt
                    else:
                        ways+=lt*rt+lf*rf
                        
            dp[(i,j,isTrue)]=ways
            return ways
        return solve(0,len(s)-1,True)
