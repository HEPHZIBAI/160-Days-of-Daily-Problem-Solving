'''
A message containing letters A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

You are given a string digits. You have to determine the total number of ways that message can be decoded.

Examples:

Input: digits = "123"
Output: 3
Explanation: "123" can be decoded as "ABC"(1, 2, 3), "LC"(12, 3) and "AW"(1, 23).
Input: digits = "90"
Output: 0
Explanation: "90" cannot be decoded, as it's an invalid string and we cannot decode '0'.
Input: digits = "05"
Output: 0
Explanation: "05" cannot be mapped to "E" because of the leading zero ("5" is different from "05"), the string is not a valid encoding message.
Constraints:
1 ≤ digits.size() ≤ 103

'''


class Solution:
	def countWays(self, digits):
		if not digits or digits[0]=='0':
		    return 0
		    
		p2,p1=1,1
		
		for i in range(1,len(digits)):
		    curr=0
		    
		    if '1'<=digits[i]<='9':
		        curr+=p1
		        
		    if '10'<=digits[i-1:i+1]<="26":
		        curr+=p2
		        
		    p2,p1=p1,curr
		    
		return p1