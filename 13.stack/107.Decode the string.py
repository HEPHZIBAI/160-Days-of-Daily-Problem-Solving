'''
Given an encoded string s, the task is to decode it. The encoding rule is :

k[encodedString], where the encodedString inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets.
Note: The test cases are generated so that the length of the output string will never exceed 105 .

Examples:

Input: s = "1[b]"
Output: "b"
Explanation: "b" is present only one time.
Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation:
1. Inner substring “2[ca]” breakdown into “caca”.
2. Now, new string becomes “3[bcaca]”
3. Similarly “3[bcaca]” becomes “bcacabcacabcaca ” which is final result.
Constraints:
1 ≤ |s| ≤ 105 
1 <= k <= 100


'''


class Solution:
    def decodedString(self, s):
        stack=[]
        num=0
        cs=""
        
        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c=='[':
                stack.append((cs,num))
                cs,num="",0
            elif c ==']':
                ls,rt=stack.pop()
                cs=ls+(cs*rt)
            else:
                cs+=c
    
        return cs