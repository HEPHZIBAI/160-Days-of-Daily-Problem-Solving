'''
Given a string of characters s, find the length of the longest prefix which is also a suffix.
Note: Prefix and suffix can be overlapping but they should not be equal to the entire string.

Examples :

Input: s = "abab"
Output: 2
Explanation: "ab" is the longest prefix and suffix. 
Input: s = "aabcdaabc"
Output: 4
Explanation: The string "aabc" is the longest prefix and suffix.
Input: s = "aaaa"
Output: 3
Explanation: "aaa" is the longest prefix and suffix. 
Constraints:
1 ≤ s.size() ≤ 106
s contains only lowercase English alphabets.
'''

class Solution:
	def longestPrefixSuffix(self, s):
		n=len(s)
		lps=[0]*n
		length=0
		i=1
		
		while i<n:
		    if s[i] == s[length]:
		        length+=1
		        lps[i]=length
		        i+=1
		    else:
		        if length!=0:
		            length=lps[length-1]
		        else:
		            lps[i]=0
		            i+=1
		            
        lon=lps[-1]
		return lon