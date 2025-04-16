'''
Given a string s, return the lexicographically largest string that can be obtained by swapping at most one pair of characters in s.

Examples:

Input: s = "768"
Output: "867"
Explanation: Swapping the 1st and 3rd characters(7 and 8 respectively), gives the lexicographically largest string.
Input: s = "333"
Output: "333"
Explanation: Performing any swaps gives the same result i.e "333".
Constraints:
1 ≤ |s| ≤ 105
'''

class Solution:
    def largestSwap(self,s):
        s=list(s)
        l={digit:i for i,digit in enumerate(s)}

        for i in range(len(s)):
            for d in map(str,range(9,int(s[i]),-1)):
                if d in l and l[d]>i:
                    s[i],s[l[d]]=s[l[d]],s[i]
                    return ''.join(s)
            
        return ''.join(s)