'''
Given a string s containing only digits, your task is to restore it by returning all possible valid IP address combinations. You can return your answer in any order.

A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255(inclusive).

Note: The numbers cannot be 0 prefixed unless they are 0. For example, 1.1.2.11 and 0.11.21.1 are valid IP addresses while 01.1.2.11 and 00.11.21.1 are not.

Examples:

Input: s = “255678166”
Output: [“25.56.78.166”, “255.6.78.166”, “255.67.8.166”, “255.67.81.66”]
Explanation: These are the only valid possible IP addresses.
Input: s = “25505011535”
Output: []
Explanation: We cannot generate a valid IP address with this string.
Constraints:
1<=s.size()<=16
s contains only digits(i.e. 0-9)
'''

class Solution:
    def generateIp(self, s):
        def isvalid(seg):
            return int(seg)<=255 and (seg=='0' or seg[0]!='0')
            
        def bt(i,p):
            if i==len(s) and len(p)==4:
                result.append('.'.join(p))
                return
            
            if len(p)>=4:
                return 
            
            for j in range(1,4):
                if i+j <=len(s):
                    seg=s[i:i+j]
                    if isvalid(seg):
                        bt(i+j,p+[seg])
                        
        result=[]
        if 4<=len(s)<=12:
            bt(0,[])
        return result
