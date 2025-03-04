'''
Given an array arr[] of positive integers. Find the number of pairs of integers whose absolute difference equals to a given number k.
Note: (a, b) and (b, a) are considered the same. Also, the same numbers at different indices are considered different.

The answer is guaranteed to fit in a 32-bit integer.

Examples:

Input: arr[] = [1, 4, 1, 4, 5], k = 3
Output: 4
Explanation: There are 4 pairs with absolute difference 3, the pairs are {1, 4}, {1, 4}, {4, 1} and {1, 4}.
Input: arr[] = [8, 16, 12, 16, 4, 0], k = 4
Output: 5
Explanation: There are 5 pairs with absolute difference 4, the pairs are {8, 12}, {8, 4}, {16, 12}, {12, 16}, {4, 0}.
Constraints:
1 <= arr.size() <= 2*105
1 <= k <= 2*105
0 <= arr[i] <= 105
'''

class Solution:
	def countPairs(self, arr, k):
	    freq={}
	    count=0
	    
	    for i in arr:
	        freq[i]=freq.get(i,0)+1
	        
	    for i in freq:
	        if k>0 and i+k in freq:
	            count+=freq[i]*freq[i+k]
	        if k>0 and i-k in freq:
	            count+=freq[i]*freq[i-k]
	    
	    return count//2