'''
Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

Examples:

Input: arr[] = [3, 30, 34, 5, 9]
Output: "9534330"
Explanation: Given numbers are [3, 30, 34, 5, 9], the arrangement "9534330" gives the largest value.
Input: arr[] = [54, 546, 548, 60]
Output: "6054854654"
Explanation: Given numbers are [54, 546, 548, 60], the arrangement "6054854654" gives the largest value.
Input: arr[] = [3, 4, 6, 5, 9]
Output: "96543"
Explanation: Given numbers are [3, 4, 6, 5, 9], the arrangement "96543" gives the largest value.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
'''

class Solution:

	def findLargest(self,arr):
	    arr=list(map(str,arr))
	    arr.sort(reverse=True,key=lambda x:x *10)
	    
	    result=''.join(arr)
	    
	    if result[0]=='0':
	        return '0'
	        
	    return result