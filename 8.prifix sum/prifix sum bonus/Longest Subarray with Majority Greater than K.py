'''
Given an array arr[] and an integer k, the task is to find the length of longest subarray in which the count of elements greater than k is more than the count of elements less than or equal to k.

Examples:

Input: arr[] = [1, 2, 3, 4, 1] , k = 2
Output: 3
Explanation: The subarray [2, 3, 4] or [3, 4, 1] satisfy the given condition, and there is no subarray of length 4 or 5 which will hold the given condition, so the answer is 3.
Input: arr[] = [6, 5, 3, 4], k = 2
Output: 4
Explanation: In the subarray [6, 5, 3, 4], there are 4 elements > 2 and 0 elements <= 2, so it is the longest subarray.
Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 106
0 <= k <= 106


'''


class Solution:
    def longestSubarray(self, arr, k):
        n=len(arr)
        t=[1 if x>k else -1 for x in arr]
        ps=0
        pm={0:-1}
        ml=0
        
        for i in range(n):
            ps+=t[i]
            
            if ps>0:
                ml=i+1
                
            if ps-1 in pm:
                ml=max(ml,i-pm[ps-1])
                
            if ps not in pm:
                pm[ps]=i
                
        return ml